from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ApiKeysService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer une clé API"""
        path = "/api-keys"
        return self._request("POST", path, data=body)

    def list(self) -> Any:
        """List API keys"""
        path = "/api-keys"
        return self._request("GET", path)

    def revoke(self, id: str) -> Any:
        """Révoquer une clé API"""
        path = "/api-keys/{id}"
        path = path.replace("{id}", str(id))
        return self._request("DELETE", path)

