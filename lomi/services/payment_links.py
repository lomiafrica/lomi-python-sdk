from typing import List, Optional
from ..models import PaymentLinks, PaymentLinksCreate, PaymentLinksUpdate
from ..client_base import ClientBase

class PaymentLinksService(ClientBase):
    """payment_links API service"""
    
    
    def list(self, **params) -> List[PaymentLinks]:
        """List payment_links"""
        return self._request("GET", "/payment-links", model=PaymentLinks, params=params)
    
    
    def get(self, id: str) -> PaymentLinks:
        """Get a single payment_link"""
        return self._request("GET", f"/payment-links/{id}", model=PaymentLinks)
    
    
    def create(self, data: PaymentLinksCreate) -> PaymentLinks:
        """Create a new payment_link"""
        return self._request("POST", "/payment-links", model=PaymentLinks, data=data)
    
    
    
