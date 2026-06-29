from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class WebhookDeliveryLogsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Obtenir un journal de livraison par ID"""
        path = "/webhook-delivery-logs/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les journaux de livraison"""
        path = "/webhook-delivery-logs"
        return self._request("GET", path, params=params)

