from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class CheckoutSessionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer une session de paiement"""
        path = "/checkout-sessions"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Obtenir une session de paiement par ID"""
        path = "/checkout-sessions/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les sessions de paiement"""
        path = "/checkout-sessions"
        return self._request("GET", path, params=params)

