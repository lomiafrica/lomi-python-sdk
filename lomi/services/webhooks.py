from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class WebhooksService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Obtenir un webhook par ID"""
        path = "/webhooks/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self) -> Any:
        """Lister les webhooks"""
        path = "/webhooks"
        return self._request("GET", path)

    def update(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Mettre à jour un webhook"""
        path = "/webhooks/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path, data=body)

