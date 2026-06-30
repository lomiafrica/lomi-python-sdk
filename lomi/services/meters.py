from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class MetersService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Create a meter"""
        path = "/meters"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Get a meter"""
        path = "/meters/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_customer_balance(self, id: str, customerId: str) -> Any:
        """Get meter balance for a customer"""
        path = "/meters/{id}/balances/{customerId}"
        path = path.replace("{id}", str(id))
        path = path.replace("{customerId}", str(customerId))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List meters"""
        path = "/meters"
        return self._request("GET", path, params=params)

    def update(self, id: str) -> Any:
        """Update a meter"""
        path = "/meters/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path)

