from typing import List, Optional
from ..models import Refunds, RefundsCreate, RefundsUpdate
from ..client_base import ClientBase

class RefundsService(ClientBase):
    """refunds API service"""
    
    
    def list(self, **params) -> List[Refunds]:
        """List refunds"""
        return self._request("GET", "/refunds", model=Refunds, params=params)
    
    
    def get(self, id: str) -> Refunds:
        """Get a single refund"""
        return self._request("GET", f"/refunds/{id}", model=Refunds)
    
    
    def create(self, data: RefundsCreate) -> Refunds:
        """Create a new refund"""
        return self._request("POST", "/refunds", model=Refunds, data=data)
    
    
    
