"""
lomi. Python SDK Client
AUTO-GENERATED - Do not edit manually
"""

import requests
from typing import Optional, Dict, Any
from .exceptions import LomiError, LomiAuthError, LomiNotFoundError


class LomiClient:
    """Main lomi. SDK client"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.lomi.africa",
        environment: str = "live"
    ):
        self.api_key = api_key
        self.base_url = base_url if environment != "test" else "https://sandbox.api.lomi.africa"
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-KEY": api_key,
            "Content-Type": "application/json",
        })
        
        # Initialize service instances
        self.accounts = AccountsService(self)
        self.organizations = OrganizationsService(self)
        self.customers = CustomersService(self)
        self.payment_requests = PaymentRequestsService(self)
        self.transactions = TransactionsService(self)
        self.refunds = RefundsService(self)
        self.products = ProductsService(self)
        self.subscriptions = SubscriptionsService(self)
        self.discount_coupons = DiscountCouponsService(self)
        self.checkout_sessions = CheckoutSessionsService(self)
        self.payment_links = PaymentLinksService(self)
        self.payouts = PayoutsService(self)
        self.beneficiary_payouts = BeneficiaryPayoutsService(self)
        self.webhooks = WebhooksService(self)
        self.webhook_delivery_logs = WebhookDeliveryLogsService(self)
        self.providers = ProvidersService(self)
    
    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make an HTTP request to the API"""
        url = f"{self.base_url}{path}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
            )
            
            if response.status_code == 401:
                raise LomiAuthError("Invalid API key", response.status_code, response.json())
            elif response.status_code == 404:
                raise LomiNotFoundError("Resource not found", response.status_code, response.json())
            elif response.status_code >= 400:
                raise LomiError(f"API error: {response.text}", response.status_code, response.json() if response.text else None)
            
            return response.json() if response.text else None
            
        except requests.RequestException as e:
            raise LomiError(f"Request failed: {str(e)}")



class AccountsService:
    """accounts API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List accounts"""
        return self._client._request("GET", "/accounts", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single account"""
        return self._client._request("GET", f"/accounts/{id}")


class OrganizationsService:
    """organizations API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List organizations"""
        return self._client._request("GET", "/organizations", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single organization"""
        return self._client._request("GET", f"/organizations/{id}")


class CustomersService:
    """customers API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List customers"""
        return self._client._request("GET", "/customers", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single customer"""
        return self._client._request("GET", f"/customers/{id}")

    def create(self, data: dict) -> dict:
        """Create a customer"""
        return self._client._request("POST", "/customers", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a customer"""
        return self._client._request("PATCH", f"/customers/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a customer"""
        return self._client._request("DELETE", f"/customers/{id}")


class PaymentRequestsService:
    """payment_requests API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List payment_requests"""
        return self._client._request("GET", "/payment-requests", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single payment_request"""
        return self._client._request("GET", f"/payment-requests/{id}")


class TransactionsService:
    """transactions API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List transactions"""
        return self._client._request("GET", "/transactions", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single transaction"""
        return self._client._request("GET", f"/transactions/{id}")


class RefundsService:
    """refunds API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List refunds"""
        return self._client._request("GET", "/refunds", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single refund"""
        return self._client._request("GET", f"/refunds/{id}")


class ProductsService:
    """products API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List products"""
        return self._client._request("GET", "/products", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single product"""
        return self._client._request("GET", f"/products/{id}")

    def create(self, data: dict) -> dict:
        """Create a product"""
        return self._client._request("POST", "/products", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a product"""
        return self._client._request("PATCH", f"/products/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a product"""
        return self._client._request("DELETE", f"/products/{id}")


class SubscriptionsService:
    """subscriptions API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List subscriptions"""
        return self._client._request("GET", "/subscriptions", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single subscription"""
        return self._client._request("GET", f"/subscriptions/{id}")

    def create(self, data: dict) -> dict:
        """Create a subscription"""
        return self._client._request("POST", "/subscriptions", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a subscription"""
        return self._client._request("PATCH", f"/subscriptions/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a subscription"""
        return self._client._request("DELETE", f"/subscriptions/{id}")


class DiscountCouponsService:
    """discount_coupons API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List discount_coupons"""
        return self._client._request("GET", "/discount-coupons", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single discount_coupon"""
        return self._client._request("GET", f"/discount-coupons/{id}")


class CheckoutSessionsService:
    """checkout_sessions API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List checkout_sessions"""
        return self._client._request("GET", "/checkout-sessions", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single checkout_session"""
        return self._client._request("GET", f"/checkout-sessions/{id}")

    def create(self, data: dict) -> dict:
        """Create a checkout_session"""
        return self._client._request("POST", "/checkout-sessions", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a checkout_session"""
        return self._client._request("PATCH", f"/checkout-sessions/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a checkout_session"""
        return self._client._request("DELETE", f"/checkout-sessions/{id}")


class PaymentLinksService:
    """payment_links API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List payment_links"""
        return self._client._request("GET", "/payment-links", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single payment_link"""
        return self._client._request("GET", f"/payment-links/{id}")

    def create(self, data: dict) -> dict:
        """Create a payment_link"""
        return self._client._request("POST", "/payment-links", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a payment_link"""
        return self._client._request("PATCH", f"/payment-links/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a payment_link"""
        return self._client._request("DELETE", f"/payment-links/{id}")


class PayoutsService:
    """payouts API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List payouts"""
        return self._client._request("GET", "/payouts", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single payout"""
        return self._client._request("GET", f"/payouts/{id}")


class BeneficiaryPayoutsService:
    """beneficiary_payouts API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List beneficiary_payouts"""
        return self._client._request("GET", "/beneficiary-payouts", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single beneficiary_payout"""
        return self._client._request("GET", f"/beneficiary-payouts/{id}")


class WebhooksService:
    """webhooks API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List webhooks"""
        return self._client._request("GET", "/webhooks", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single webhook"""
        return self._client._request("GET", f"/webhooks/{id}")

    def create(self, data: dict) -> dict:
        """Create a webhook"""
        return self._client._request("POST", "/webhooks", data=data)

    def update(self, id: str, data: dict) -> dict:
        """Update a webhook"""
        return self._client._request("PATCH", f"/webhooks/{id}", data=data)

    def delete(self, id: str) -> dict:
        """Delete a webhook"""
        return self._client._request("DELETE", f"/webhooks/{id}")


class ProvidersService:
    """providers API service"""

    def __init__(self, client: LomiClient):
        self._client = client

    def list(self, **params) -> list:
        """List providers"""
        return self._client._request("GET", "/providers", params=params)

    def get(self, id: str) -> dict:
        """Get a single provider"""
        return self._client._request("GET", f"/providers/{id}")



class WebhookDeliveryLogsService:
    """webhook_delivery_logs API service"""
    
    def __init__(self, client: LomiClient):
        self._client = client
    
    def list(self, **params) -> list:
        """List webhook_delivery_logs"""
        return self._client._request("GET", "/webhook-delivery-logs", params=params)
    
    def get(self, id: str) -> dict:
        """Get a single webhook_delivery_log"""
        return self._client._request("GET", f"/webhook-delivery-logs/{id}")

