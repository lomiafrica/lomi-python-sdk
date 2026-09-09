"""lomi. Network: Lomi-Account scoping, transfers, balance, login links, sessions.

HTTP is mocked at ``requests.Session.request`` so no network access is needed.
"""
import unittest
from unittest import mock

from lomi import LomiClient
from lomi.network import is_confirmation_required


class _FakeResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code
        self.content = b"{}"
        self.text = "{}"

    def json(self):
        return self._payload


def _client(**kwargs):
    c = LomiClient(api_key="lomi_sk_test_x", **kwargs)
    return c


def _sent_headers(session, call):
    """Merge session headers with per-request headers the way requests does."""
    merged = dict(session.headers)
    for k, v in (call.kwargs.get("headers") or {}).items():
        if v is None:
            merged.pop(k, None)
        else:
            merged[k] = v
    return merged


class TestAccountScoping(unittest.TestCase):
    def test_client_account_sets_header_on_every_request(self):
        c = _client(account="acct_member")
        self.assertEqual(c.session.headers["Lomi-Account"], "acct_member")
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse({"data": []})
        ) as req:
            c.customers.list()
        self.assertEqual(
            _sent_headers(c.session, req.call_args)["Lomi-Account"], "acct_member"
        )

    def test_no_account_by_default(self):
        c = _client()
        self.assertIsNone(c.lomi_account)
        self.assertNotIn("Lomi-Account", c.session.headers)

    def test_with_account_returns_scoped_copy(self):
        c = _client(environment="test")
        scoped = c.with_account("acct_scoped")
        self.assertIsNot(scoped, c)
        self.assertEqual(scoped.lomi_account, "acct_scoped")
        self.assertEqual(scoped.base_url, c.base_url)
        self.assertEqual(scoped.api_key, c.api_key)
        self.assertNotIn("Lomi-Account", c.session.headers)
        self.assertIsNone(c.with_account(None).lomi_account)

    def test_per_request_account_override(self):
        c = _client(account="acct_default")
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse([])
        ) as req:
            c.balance.retrieve(account="acct_other")
        headers = _sent_headers(c.session, req.call_args)
        self.assertEqual(headers["Lomi-Account"], "acct_other")
        self.assertEqual(req.call_args.kwargs["url"], f"{c.base_url}/accounts/balance")

    def test_balance_defaults_to_client_account(self):
        c = _client(account="acct_default")
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse([])
        ) as req:
            c.balance.retrieve()
        self.assertEqual(
            _sent_headers(c.session, req.call_args)["Lomi-Account"], "acct_default"
        )


class TestTransfers(unittest.TestCase):
    def test_create_strips_lomi_account_and_sends_idempotency_key(self):
        c = _client(account="acct_default")
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse({"id": "tr_1"})
        ) as req:
            out = c.transfers.create(
                amount=5000,
                currency_code="XOF",
                destination="acct_seller",
                transfer_group="order_42",
                idempotency_key="idem-1",
            )
        self.assertEqual(out["id"], "tr_1")
        call = req.call_args
        self.assertEqual(call.kwargs["method"], "POST")
        self.assertEqual(call.kwargs["url"], f"{c.base_url}/transfers")
        self.assertEqual(
            call.kwargs["json"],
            {
                "amount": 5000,
                "currency_code": "XOF",
                "destination": "acct_seller",
                "transfer_group": "order_42",
            },
        )
        headers = _sent_headers(c.session, call)
        self.assertNotIn("Lomi-Account", headers)
        self.assertEqual(headers["Idempotency-Key"], "idem-1")

    def test_create_generates_idempotency_key(self):
        c = _client()
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse({"id": "tr_1"})
        ) as req:
            c.transfers.create(amount=1, currency_code="XOF", destination="acct_x")
        key = req.call_args.kwargs["headers"]["Idempotency-Key"]
        self.assertTrue(key and len(key) >= 32)

    def test_create_confirmed_runs_two_step_flow_with_one_key(self):
        c = _client()
        preview = {
            "requires_confirmation": True,
            "confirmation_token": "tok_1",
            "expires_at": "2026-01-01T00:00:00Z",
            "preview": {"amount": 100},
        }
        self.assertTrue(is_confirmation_required(preview))
        responses = [_FakeResponse(preview), _FakeResponse({"id": "tr_2", "status": "paid"})]
        with mock.patch.object(c.session, "request", side_effect=responses) as req:
            out = c.transfers.create_confirmed(
                amount=100, currency_code="XOF", destination="acct_x"
            )
        self.assertEqual(out["id"], "tr_2")
        self.assertEqual(req.call_count, 2)
        first, second = req.call_args_list
        self.assertNotIn("confirmation_token", first.kwargs["json"])
        self.assertEqual(second.kwargs["json"]["confirmation_token"], "tok_1")
        self.assertEqual(
            first.kwargs["headers"]["Idempotency-Key"],
            second.kwargs["headers"]["Idempotency-Key"],
        )

    def test_list_retrieve_reverse(self):
        c = _client()
        page = {"data": [{"id": "tr_1"}], "has_more": False, "next_cursor": None}
        with mock.patch.object(
            c.session, "request", return_value=_FakeResponse(page)
        ) as req:
            c.transfers.list(destination="acct_x", transfer_type="separate", limit=10)
            c.transfers.retrieve("tr_1")
            c.transfers.reverse("tr_1", amount=50, idempotency_key="idem-r")
        list_call, get_call, rev_call = req.call_args_list
        self.assertEqual(
            list_call.kwargs["params"],
            {"destination": "acct_x", "transfer_type": "separate", "limit": 10},
        )
        self.assertEqual(get_call.kwargs["url"], f"{c.base_url}/transfers/tr_1")
        self.assertEqual(rev_call.kwargs["url"], f"{c.base_url}/transfers/tr_1/reversals")
        self.assertEqual(rev_call.kwargs["json"], {"amount": 50})
        self.assertEqual(rev_call.kwargs["headers"]["Idempotency-Key"], "idem-r")

    def test_list_all_paginates(self):
        c = _client()
        pages = [
            _FakeResponse({"data": [{"id": "tr_1"}], "has_more": True, "next_cursor": "c2"}),
            _FakeResponse({"data": [{"id": "tr_2"}], "has_more": False, "next_cursor": None}),
        ]
        with mock.patch.object(c.session, "request", side_effect=pages) as req:
            ids = [t["id"] for t in c.transfers.list_all(destination="acct_x")]
        self.assertEqual(ids, ["tr_1", "tr_2"])
        self.assertEqual(req.call_args_list[1].kwargs["params"]["cursor"], "c2")


class TestNetworkResources(unittest.TestCase):
    def test_create_login_link(self):
        c = _client(account="acct_default")
        with mock.patch.object(
            c.session,
            "request",
            return_value=_FakeResponse({"object": "login_link", "url": "https://x"}),
        ) as req:
            out = c.network.accounts.create_login_link("acct_member")
        self.assertEqual(out["object"], "login_link")
        call = req.call_args
        self.assertEqual(call.kwargs["method"], "POST")
        self.assertEqual(
            call.kwargs["url"], f"{c.base_url}/network/accounts/acct_member/login_links"
        )
        self.assertNotIn("Lomi-Account", _sent_headers(c.session, call))

    def test_create_account_session(self):
        c = _client()
        with mock.patch.object(
            c.session,
            "request",
            return_value=_FakeResponse({"object": "account_session", "client_secret": "s"}),
        ) as req:
            c.network.account_sessions.create("acct_member")
            c.network.account_sessions.create(
                "acct_member", components={"onboarding": {"enabled": True}}
            )
        first, second = req.call_args_list
        self.assertEqual(first.kwargs["url"], f"{c.base_url}/network/account-sessions")
        self.assertEqual(first.kwargs["json"], {"account": "acct_member"})
        self.assertEqual(
            second.kwargs["json"],
            {"account": "acct_member", "components": {"onboarding": {"enabled": True}}},
        )


if __name__ == "__main__":
    unittest.main()
