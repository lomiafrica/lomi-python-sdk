"""lomi. Python SDK — generated from OpenAPI + public allowlist."""

import requests
from typing import Optional, Dict, Any

from .exceptions import LomiError, LomiAuthError, LomiNotFoundError
from .network import BalanceResource, NetworkResource, TransfersResource
from .services import *

def _flatten_data(data):
    if data is None:
        return None
    if hasattr(data, "model_dump"):
        return data.model_dump(exclude_unset=True)
    if hasattr(data, "dict"):
        return data.dict(exclude_unset=True)
    return data


class LomiClient:
    """Merchant API client (public routes only).

    account="acct_..." (lomi. Network) sends Lomi-Account on every request so
    calls run on behalf of that Member Account (direct charges). Use
    with_account() for a scoped copy, or the account= kwarg on client.balance
    for a single call.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.lomi.africa",
        environment: str = "live",
        account: Optional[str] = None,
    ):
        self.api_key = api_key
        test_host = environment in ("test", "sandbox") or (
            isinstance(environment, str) and environment.lower() == "test"
        )
        self.base_url = (
            base_url if not test_host else "https://sandbox.api.lomi.africa"
        )
        # stored as lomi_account: "account" is the generated /account/* service
        self.lomi_account = account or None
        self.session = requests.Session()
        self.session.headers.update(
            {"X-API-KEY": api_key, "Content-Type": "application/json"}
        )
        if self.lomi_account:
            self.session.headers["Lomi-Account"] = self.lomi_account
        self.account = AccountService(self)
        self.accounts = AccountsService(self)
        self.api_keys = ApiKeysService(self)
        self.charges = ChargesService(self)
        self.checkout_sessions = CheckoutSessionsService(self)
        self.coupons = CouponsService(self)
        self.customers = CustomersService(self)
        self.disputes = DisputesService(self)
        self.exports = ExportsService(self)
        self.finance = FinanceService(self)
        self.invoices = InvoicesService(self)
        self.logs = LogsService(self)
        self.merchants = MerchantsService(self)
        self.meters = MetersService(self)
        self.organizations = OrganizationsService(self)
        self.payment_links = PaymentLinksService(self)
        self.payment_requests = PaymentRequestsService(self)
        self.payout_methods = PayoutMethodsService(self)
        self.payouts = PayoutsService(self)
        self.products = ProductsService(self)
        self.providers = ProvidersService(self)
        self.refunds = RefundsService(self)
        self.risk_assessments = RiskAssessmentsService(self)
        self.settings = SettingsService(self)
        self.settlements = SettlementsService(self)
        self.subscriptions = SubscriptionsService(self)
        self.support_requests = SupportRequestsService(self)
        self.team = TeamService(self)
        self.transactions = TransactionsService(self)
        self.usage = UsageService(self)
        self.webhooks = WebhooksService(self)

        # lomi. Network (hand-written, see lomi/network.py)
        self.transfers = TransfersResource(self)
        self.balance = BalanceResource(self)
        self.network = NetworkResource(self)

    def with_account(self, account: Optional[str]) -> "LomiClient":
        """Return a client scoped to a Member Account (Lomi-Account: acct_...).

        with_account(None) returns an Operator-scoped client (no header).
        """
        return LomiClient(
            api_key=self.api_key,
            base_url=self.base_url,
            environment="live",
            account=account,
        )

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        account: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        json_data = _flatten_data(data)
        headers: Dict[str, Optional[str]] = {}
        if account is not None:
            # "" removes the session-level Lomi-Account for this call.
            headers["Lomi-Account"] = account or None
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
                headers=headers or None,
            )

            if response.status_code == 401:
                raise LomiAuthError(
                    "Invalid API key",
                    response.status_code,
                    response.json() if response.content else None,
                )
            if response.status_code == 404:
                raise LomiNotFoundError(
                    "Resource not found",
                    response.status_code,
                    response.json() if response.content else None,
                )
            if response.status_code >= 400:
                raise LomiError(
                    f"API error: {response.text}",
                    response.status_code,
                    response.json() if response.text else None,
                )

            return response.json() if response.content else None
        except requests.RequestException as e:
            raise LomiError(f"Request failed: {type(e).__name__}: {e}") from e

