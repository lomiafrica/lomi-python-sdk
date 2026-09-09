"""lomi. Network resources (hand-written, not regenerated from OpenAPI).

lomi. Network lets an Operator organization charge on behalf of Member
Accounts (``acct_…``):

* **Direct charges**: call the regular endpoints with ``Lomi-Account`` set
  (``LomiClient(api_key=..., account="acct_…")`` or ``client.with_account(...)``).
* **Destination charges**: charge on your own account and pass
  ``transfer_data={"destination": "acct_…"}`` (+ ``application_fee_amount``).
* **Separate charges and transfers**: charge with a ``transfer_group`` and move
  funds later with :meth:`TransfersResource.create`.

Transfers, login links and account sessions are Operator-level calls: they use
your Operator API key and never send ``Lomi-Account`` (this module strips the
client default for those routes).

Two-step money confirmation
---------------------------
``POST /transfers`` and ``POST /transfers/{id}/reversals`` follow the same
preview/confirm flow as refunds and payouts. The first call (without
``confirmation_token``) returns::

    {"requires_confirmation": True, "confirmation_token": "…",
     "expires_at": "…", "preview": {...}}

Call again with ``confirmation_token`` set to execute. ``Idempotency-Key`` is
required on the executing call; the SDK generates a UUID when you do not pass
``idempotency_key`` and :meth:`TransfersResource.create_confirmed` /
:meth:`TransfersResource.reverse_confirmed` reuse the same key for both calls.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict, Iterator, Optional

from .client_base import ClientBase

# Explicitly send no Lomi-Account header (Operator-level routes).
OPERATOR = ""


def is_confirmation_required(value: Any) -> bool:
    """True when the API returned a money-confirmation preview."""
    return isinstance(value, dict) and value.get("requires_confirmation") is True


def _drop_none(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in payload.items() if v is not None}


class TransfersResource(ClientBase):
    """``/transfers`` — move Operator funds to Member Accounts."""

    def create(
        self,
        amount: int,
        currency_code: str,
        destination: str,
        transfer_group: Optional[str] = None,
        source_transaction_id: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        confirmation_token: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a transfer (``POST /transfers``).

        Without ``confirmation_token`` the API answers with a preview; call again
        with the returned token to execute. Pass the same ``idempotency_key`` on
        both calls (auto-generated when omitted).
        """
        body = _drop_none(
            {
                "amount": amount,
                "currency_code": currency_code,
                "destination": destination,
                "transfer_group": transfer_group,
                "source_transaction_id": source_transaction_id,
                "description": description,
                "metadata": metadata,
                "confirmation_token": confirmation_token,
            }
        )
        return self._request(
            "POST",
            "/transfers",
            data=body,
            account=OPERATOR,
            idempotency_key=idempotency_key or str(uuid.uuid4()),
        )

    def create_confirmed(self, **kwargs: Any) -> Dict[str, Any]:
        """Preview then execute a transfer (two HTTP calls, one idempotency key)."""
        kwargs.setdefault("idempotency_key", str(uuid.uuid4()))
        kwargs.pop("confirmation_token", None)
        first = self.create(**kwargs)
        if not is_confirmation_required(first):
            return first
        second = self.create(confirmation_token=first["confirmation_token"], **kwargs)
        if is_confirmation_required(second):
            raise RuntimeError("lomi. API asked for confirmation twice; aborting transfer.")
        return second

    def list(
        self,
        destination: Optional[str] = None,
        transfer_group: Optional[str] = None,
        source_transaction_id: Optional[str] = None,
        transfer_type: Optional[str] = None,
        cursor: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Dict[str, Any]:
        """List transfers created by your Network (``GET /transfers``)."""
        params = _drop_none(
            {
                "destination": destination,
                "transfer_group": transfer_group,
                "source_transaction_id": source_transaction_id,
                "transfer_type": transfer_type,
                "cursor": cursor,
                "limit": limit,
            }
        )
        return self._request("GET", "/transfers", params=params, account=OPERATOR)

    def list_all(self, **filters: Any) -> Iterator[Dict[str, Any]]:
        """Iterate every transfer across cursor pages."""
        cursor = filters.pop("cursor", None)
        while True:
            page = self.list(cursor=cursor, **filters)
            for item in page.get("data", []):
                yield item
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            cursor = page["next_cursor"]

    def retrieve(self, id: str) -> Dict[str, Any]:
        """Retrieve one transfer (``GET /transfers/{id}``)."""
        return self._request("GET", f"/transfers/{id}", account=OPERATOR)

    get = retrieve

    def reverse(
        self,
        id: str,
        amount: Optional[int] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        confirmation_token: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Reverse a transfer fully or partially (``POST /transfers/{id}/reversals``).

        Same two-step confirmation as :meth:`create`.
        """
        body = _drop_none(
            {
                "amount": amount,
                "description": description,
                "metadata": metadata,
                "confirmation_token": confirmation_token,
            }
        )
        return self._request(
            "POST",
            f"/transfers/{id}/reversals",
            data=body,
            account=OPERATOR,
            idempotency_key=idempotency_key or str(uuid.uuid4()),
        )

    def reverse_confirmed(self, id: str, **kwargs: Any) -> Dict[str, Any]:
        """Preview then execute a reversal (two HTTP calls, one idempotency key)."""
        kwargs.setdefault("idempotency_key", str(uuid.uuid4()))
        kwargs.pop("confirmation_token", None)
        first = self.reverse(id, **kwargs)
        if not is_confirmation_required(first):
            return first
        second = self.reverse(id, confirmation_token=first["confirmation_token"], **kwargs)
        if is_confirmation_required(second):
            raise RuntimeError("lomi. API asked for confirmation twice; aborting reversal.")
        return second


class BalanceResource(ClientBase):
    """``GET /accounts/balance`` — your balance, or a Member Account's with ``account``."""

    def retrieve(self, account: Optional[str] = None) -> Any:
        """Balance rows ``[{currency_code, balance, last_updated}]``.

        ``account="acct_…"`` reads the Member Account balance (``Lomi-Account``).
        Defaults to the client-level account when set.
        """
        return self._request("GET", "/accounts/balance", account=account)

    get = retrieve


class NetworkAccountsResource(ClientBase):
    """``/network/accounts/{account}/…`` — Member Account helpers."""

    def create_login_link(self, account: str) -> Dict[str, Any]:
        """Single-use dashboard login link for a Member Account.

        ``POST /network/accounts/{account}/login_links`` →
        ``{object: "login_link", account, url, created_at, expires_at}``.
        """
        return self._request(
            "POST", f"/network/accounts/{account}/login_links", account=OPERATOR
        )


class NetworkAccountSessionsResource(ClientBase):
    """``/network/account-sessions`` — client secrets for embedded components."""

    def create(
        self,
        account: str,
        components: Optional[Dict[str, Dict[str, bool]]] = None,
    ) -> Dict[str, Any]:
        """Create an account session for embedded Member onboarding/payments UI.

        ``components`` keys: ``onboarding``, ``payments``, ``payouts``,
        ``balance``, ``notification_banner`` (each ``{"enabled": bool}``).
        Returns ``{object: "account_session", account, client_secret,
        expires_at, components, embed_base_url}``.
        """
        body: Dict[str, Any] = {"account": account}
        if components is not None:
            body["components"] = components
        return self._request(
            "POST", "/network/account-sessions", data=body, account=OPERATOR
        )


class NetworkResource(ClientBase):
    """``client.network`` — login links and account sessions."""

    def __init__(self, client: Any):
        super().__init__(client)
        self.accounts = NetworkAccountsResource(client)
        self.account_sessions = NetworkAccountSessionsResource(client)
