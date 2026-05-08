from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class TransactionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Obtenir une transaction par ID"""
        path = "/transactions/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les transactions"""
        path = "/transactions"
        return self._request("GET", path, params=params)

