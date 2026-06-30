from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class PaymentLinksService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un lien de paiement"""
        path = "/payment-links"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Obtenir un lien de paiement par ID"""
        path = "/payment-links/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les liens de paiement"""
        path = "/payment-links"
        return self._request("GET", path, params=params)

