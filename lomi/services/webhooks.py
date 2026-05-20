from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class WebhooksService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Créer un webhook"""
        path = "/webhooks"
        return self._request("POST", path)

    def delete(self, id: str) -> Any:
        """Supprimer un webhook"""
        path = "/webhooks/{id}"
        path = path.replace("{id}", str(id))
        return self._request("DELETE", path)

    def get(self, id: str) -> Any:
        """Obtenir un webhook par ID"""
        path = "/webhooks/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self) -> Any:
        """Lister les webhooks"""
        path = "/webhooks"
        return self._request("GET", path)

    def retry_delivery(self, webhookId: str, logId: str) -> Any:
        """Relancer une livraison webhook"""
        path = "/webhooks/{webhookId}/logs/{logId}/retry"
        path = path.replace("{webhookId}", str(webhookId))
        path = path.replace("{logId}", str(logId))
        return self._request("POST", path)

    def test(self, id: str) -> Any:
        """Envoyer un événement test au webhook"""
        path = "/webhooks/{id}/test"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def update(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Mettre à jour un webhook"""
        path = "/webhooks/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path, data=body)

