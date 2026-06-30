from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class SubscriptionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def cancel(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Résilier un abonnement"""
        path = "/subscriptions/{id}/cancel"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("POST", path, data=body)

    def find_by_customer(self, customerId: str) -> Any:
        """Abonnements d’un client"""
        path = "/subscriptions/customer/{customerId}"
        path = path.replace("{customerId}", _safe_path_param(customerId))
        return self._request("GET", path)

    def get(self, id: str) -> Any:
        """Obtenir un abonnement par ID"""
        path = "/subscriptions/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les abonnements"""
        path = "/subscriptions"
        return self._request("GET", path, params=params)

    def update(self, id: str) -> Any:
        """Mettre à jour un abonnement"""
        path = "/subscriptions/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("PATCH", path)

