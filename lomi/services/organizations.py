from typing import List, Optional
from ..models import Organizations, OrganizationsCreate, OrganizationsUpdate
from ..client_base import ClientBase

class OrganizationsService(ClientBase):
    """organizations API service"""
    
    
    def list(self, **params) -> List[Organizations]:
        """List organizations"""
        return self._request("GET", "/organizations", model=Organizations, params=params)
    
    
    def get(self, id: str) -> Organizations:
        """Get a single organization"""
        return self._request("GET", f"/organizations/{id}", model=Organizations)
    
    
    
    
