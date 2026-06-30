from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class SettlementsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def find_all(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List settlement periods"""
        path = "/settlements"
        return self._request("GET", path, params=params)

    def find_transactions(self, id: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """List transactions in a settlement period"""
        path = "/settlements/{id}/transactions"
        path = path.replace("{id}", str(id))
        return self._request("GET", path, params=params)

