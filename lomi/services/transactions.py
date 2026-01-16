from typing import List, Optional
from ..models import Transactions, TransactionsCreate, TransactionsUpdate
from ..client_base import ClientBase

class TransactionsService(ClientBase):
    """transactions API service"""
    
    
    def list(self, **params) -> List[Transactions]:
        """List transactions"""
        return self._request("GET", "/transactions", model=Transactions, params=params)
    
    
    def get(self, id: str) -> Transactions:
        """Get a single transaction"""
        return self._request("GET", f"/transactions/{id}", model=Transactions)
    
    
    
    
