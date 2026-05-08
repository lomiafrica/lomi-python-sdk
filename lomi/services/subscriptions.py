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

    def find_by_customer(self, customerId: str) -> Any:
        """Abonnements d’un client"""
        path = "/subscriptions/customer/{customerId}"
        path = path.replace("{customerId}", str(customerId))
        return self._request("GET", path)

    def get(self, id: str) -> Any:
        """Obtenir un abonnement par ID"""
        path = "/subscriptions/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les abonnements"""
        path = "/subscriptions"
        return self._request("GET", path, params=params)

