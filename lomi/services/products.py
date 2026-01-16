from typing import List, Optional
from ..models import Products, ProductsCreate, ProductsUpdate
from ..client_base import ClientBase

class ProductsService(ClientBase):
    """products API service"""
    
    
    def list(self, **params) -> List[Products]:
        """List products"""
        return self._request("GET", "/products", model=Products, params=params)
    
    
    def get(self, id: str) -> Products:
        """Get a single product"""
        return self._request("GET", f"/products/{id}", model=Products)
    
    
    def create(self, data: ProductsCreate) -> Products:
        """Create a new product"""
        return self._request("POST", "/products", model=Products, data=data)
    
    
    
