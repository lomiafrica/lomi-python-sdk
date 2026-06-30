from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class MerchantsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Get merchant details"""
        path = "/merchants/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_arr(self, id: str) -> Any:
        """Get merchant ARR"""
        path = "/merchants/{id}/arr"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_balance(self, id: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Get merchant account balance for a currency"""
        path = "/merchants/{id}/balance"
        path = path.replace("{id}", str(id))
        return self._request("GET", path, params=params)

    def get_mrr(self, id: str) -> Any:
        """Get merchant MRR"""
        path = "/merchants/{id}/mrr"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

