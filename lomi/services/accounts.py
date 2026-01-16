from typing import List, Optional
from ..models import Accounts, AccountsCreate, AccountsUpdate
from ..client_base import ClientBase

class AccountsService(ClientBase):
    """accounts API service"""
    
    
    def list(self, **params) -> List[Accounts]:
        """List accounts"""
        return self._request("GET", "/accounts", model=Accounts, params=params)
    
    
    def get(self, id: str) -> Accounts:
        """Get a single account"""
        return self._request("GET", f"/accounts/{id}", model=Accounts)
    
    
    
    
