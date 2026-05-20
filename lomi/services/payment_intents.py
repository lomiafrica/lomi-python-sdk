from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PaymentIntentsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def cancel(self, id: str) -> Any:
        """Annuler un intent de paiement carte"""
        path = "/payment-intents/{id}/cancel"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un intent de paiement carte (client_secret)"""
        path = "/payment-intents"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Récupérer un intent de paiement carte"""
        path = "/payment-intents/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

