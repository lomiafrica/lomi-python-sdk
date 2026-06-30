from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class DisputesService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Obtenir un litige"""
        path = "/disputes/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les litiges"""
        path = "/disputes"
        return self._request("GET", path, params=params)

