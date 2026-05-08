from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class CustomersService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un client"""
        path = "/customers"
        return self._request("POST", path, data=body)

    def delete(self, id: str) -> Any:
        """Supprimer un client"""
        path = "/customers/{id}"
        path = path.replace("{id}", str(id))
        return self._request("DELETE", path)

    def get(self, id: str) -> Any:
        """Obtenir un client par ID"""
        path = "/customers/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_transactions(self, id: str) -> Any:
        """Transactions du client"""
        path = "/customers/{id}/transactions"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les clients"""
        path = "/customers"
        return self._request("GET", path, params=params)

    def update(self, id: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Mettre à jour un client"""
        path = "/customers/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path, data=body)

