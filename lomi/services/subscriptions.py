from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class SubscriptionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def cancel(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Résilier un abonnement"""
        path = "/subscriptions/{id}/cancel"
        path = path.replace("{id}", str(id))
        return self._request("POST", path, data=body)

    def change_plan(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Changer le plan tarifaire"""
        path = "/subscriptions/{id}/change-plan"
        path = path.replace("{id}", str(id))
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Obtenir un abonnement par ID"""
        path = "/subscriptions/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_usage(self, id: str) -> Any:
        """Get meter usage for a subscription"""
        path = "/subscriptions/{id}/usage"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les abonnements"""
        path = "/subscriptions"
        return self._request("GET", path, params=params)

    def resume(self, id: str) -> Any:
        """Annuler une résiliation planifiée"""
        path = "/subscriptions/{id}/resume"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def update(self, id: str) -> Any:
        """Mettre à jour un abonnement"""
        path = "/subscriptions/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path)

