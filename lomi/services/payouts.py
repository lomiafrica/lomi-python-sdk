from typing import List, Optional
from ..models import Payouts, PayoutsCreate, PayoutsUpdate
from ..client_base import ClientBase

class PayoutsService(ClientBase):
    """payouts API service"""
    
    
    def list(self, **params) -> List[Payouts]:
        """List payouts"""
        return self._request("GET", "/payouts", model=Payouts, params=params)
    
    
    def get(self, id: str) -> Payouts:
        """Get a single payout"""
        return self._request("GET", f"/payouts/{id}", model=Payouts)
    
    
    def create(self, data: PayoutsCreate) -> Payouts:
        """Create a new payout"""
        return self._request("POST", "/payouts", model=Payouts, data=data)
    
    
    
