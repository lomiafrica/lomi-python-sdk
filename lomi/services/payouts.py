from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class PayoutsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Créer un virement"""
        path = "/payouts"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Obtenir un virement"""
        path = "/payouts/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les virements"""
        path = "/payouts"
        return self._request("GET", path, params=params)

