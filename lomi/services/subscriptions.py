from typing import List, Optional
from ..models import Subscriptions, SubscriptionsCreate, SubscriptionsUpdate
from ..client_base import ClientBase

class SubscriptionsService(ClientBase):
    """subscriptions API service"""
    
    
    def list(self, **params) -> List[Subscriptions]:
        """List subscriptions"""
        return self._request("GET", "/subscriptions", model=Subscriptions, params=params)
    
    
    def get(self, id: str) -> Subscriptions:
        """Get a single subscription"""
        return self._request("GET", f"/subscriptions/{id}", model=Subscriptions)
    
    
    
    def update(self, id: str, data: SubscriptionsUpdate) -> Subscriptions:
        """Update a subscription"""
        return self._request("PATCH", f"/subscriptions/{id}", model=Subscriptions, data=data)
    
    
