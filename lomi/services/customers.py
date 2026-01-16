from typing import List, Optional
from ..models import Customers, CustomersCreate, CustomersUpdate
from ..client_base import ClientBase

class CustomersService(ClientBase):
    """customers API service"""
    
    
    def list(self, **params) -> List[Customers]:
        """List customers"""
        return self._request("GET", "/customers", model=Customers, params=params)
    
    
    def get(self, id: str) -> Customers:
        """Get a single customer"""
        return self._request("GET", f"/customers/{id}", model=Customers)
    
    
    def create(self, data: CustomersCreate) -> Customers:
        """Create a new customer"""
        return self._request("POST", "/customers", model=Customers, data=data)
    
    
    def update(self, id: str, data: CustomersUpdate) -> Customers:
        """Update a customer"""
        return self._request("PATCH", f"/customers/{id}", model=Customers, data=data)
    
    
    def delete(self, id: str) -> None:
        """Delete a customer"""
        return self._request("DELETE", f"/customers/{id}")
    
