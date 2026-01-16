from typing import List, Optional
from ..models import PaymentRequests, PaymentRequestsCreate, PaymentRequestsUpdate
from ..client_base import ClientBase

class PaymentRequestsService(ClientBase):
    """payment_requests API service"""
    
    
    def list(self, **params) -> List[PaymentRequests]:
        """List payment_requests"""
        return self._request("GET", "/payment-requests", model=PaymentRequests, params=params)
    
    
    def get(self, id: str) -> PaymentRequests:
        """Get a single payment_request"""
        return self._request("GET", f"/payment-requests/{id}", model=PaymentRequests)
    
    
    def create(self, data: PaymentRequestsCreate) -> PaymentRequests:
        """Create a new payment_request"""
        return self._request("POST", "/payment-requests", model=PaymentRequests, data=data)
    
    
    
