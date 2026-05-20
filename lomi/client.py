"""lomi. Python SDK — generated from OpenAPI + public allowlist."""

import requests
from typing import Optional, Dict, Any

from .exceptions import LomiError, LomiAuthError, LomiNotFoundError
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
    """Merchant API client (public routes only)."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.lomi.africa",
        environment: str = "live",
    ):
        self.api_key = api_key
        test_host = environment in ("test", "sandbox") or (
            isinstance(environment, str) and environment.lower() == "test"
        )
        self.base_url = (
            base_url if not test_host else "https://sandbox.api.lomi.africa"
        )
        self.session = requests.Session()
        self.session.headers.update(
            {"X-API-KEY": api_key, "Content-Type": "application/json"}
        )
        self.accounts = AccountsService(self)
        self.beneficiary_payouts = BeneficiaryPayoutsService(self)
        self.charge = ChargeService(self)
        self.charges = ChargesService(self)
        self.checkout_sessions = CheckoutSessionsService(self)
        self.customers = CustomersService(self)
        self.customer_subscriptions = CustomerSubscriptionsService(self)
        self.discount_coupons = DiscountCouponsService(self)
        self.merchants = MerchantsService(self)
        self.organizations = OrganizationsService(self)
        self.payment_intents = PaymentIntentsService(self)
        self.payment_links = PaymentLinksService(self)
        self.payment_requests = PaymentRequestsService(self)
        self.payout = PayoutService(self)
        self.payouts = PayoutsService(self)
        self.products = ProductsService(self)
        self.providers = ProvidersService(self)
        self.refunds = RefundsService(self)
        self.subscriptions = SubscriptionsService(self)
        self.transactions = TransactionsService(self)
        self.webhook_delivery_logs = WebhookDeliveryLogsService(self)
        self.webhooks = WebhooksService(self)

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        json_data = _flatten_data(data)
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
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

