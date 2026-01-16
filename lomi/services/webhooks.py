from typing import List, Optional
from ..models import Webhooks, WebhooksCreate, WebhooksUpdate
from ..client_base import ClientBase

class WebhooksService(ClientBase):
    """webhooks API service"""
    
    
    def list(self, **params) -> List[Webhooks]:
        """List webhooks"""
        return self._request("GET", "/webhooks", model=Webhooks, params=params)
    
    
    def get(self, id: str) -> Webhooks:
        """Get a single webhook"""
        return self._request("GET", f"/webhooks/{id}", model=Webhooks)
    
    
    
    def update(self, id: str, data: WebhooksUpdate) -> Webhooks:
        """Update a webhook"""
        return self._request("PATCH", f"/webhooks/{id}", model=Webhooks, data=data)
    
    
