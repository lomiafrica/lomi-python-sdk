"""
lomi. Python SDK Client
AUTO-GENERATED - Do not edit manually
"""

import requests
from typing import Optional, Dict, Any, List, Type, TypeVar
from .exceptions import LomiError, LomiAuthError, LomiNotFoundError
from .models import *
from .services import *
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

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
    
    def _request(
        self,
        method: str,
        path: str,
        model: Type[T] = None,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Make an HTTP request to the API"""
        url = f"{self.base_url}{path}"
        
        # Convert Pydantic models to dict if passed as data
        json_data = data
        if hasattr(data, 'dict'):
             json_data = data.dict(exclude_unset=True)

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
            )
            
            if response.status_code == 401:
                raise LomiAuthError("Invalid API key", response.status_code, response.json())
            elif response.status_code == 404:
                raise LomiNotFoundError("Resource not found", response.status_code, response.json())
            elif response.status_code >= 400:
                raise LomiError(f"API error: {response.text}", response.status_code, response.json() if response.text else None)
            
            resp_data = response.json() if response.text else None
            
            # If model class provided, parse response
            if model and resp_data:
                if isinstance(resp_data, list):
                    return [model(**item) for item in resp_data]
                return model(**resp_data)
                
            return resp_data
            
        except requests.RequestException as e:
            raise LomiError(f"Request failed: {str(e)}")
