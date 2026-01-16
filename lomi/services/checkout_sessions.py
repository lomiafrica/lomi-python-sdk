from typing import List, Optional
from ..models import CheckoutSessions, CheckoutSessionsCreate, CheckoutSessionsUpdate
from ..client_base import ClientBase

class CheckoutSessionsService(ClientBase):
    """checkout_sessions API service"""
    
    
    def list(self, **params) -> List[CheckoutSessions]:
        """List checkout_sessions"""
        return self._request("GET", "/checkout-sessions", model=CheckoutSessions, params=params)
    
    
    def get(self, id: str) -> CheckoutSessions:
        """Get a single checkout_session"""
        return self._request("GET", f"/checkout-sessions/{id}", model=CheckoutSessions)
    
    
    def create(self, data: CheckoutSessionsCreate) -> CheckoutSessions:
        """Create a new checkout_session"""
        return self._request("POST", "/checkout-sessions", model=CheckoutSessions, data=data)
    
    
    
