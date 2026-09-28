from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PayoutsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un virement"""
        path = "/payouts"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Obtenir un virement"""
        path = "/payouts/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les virements"""
        path = "/payouts"
        return self._request("GET", path, params=params)

