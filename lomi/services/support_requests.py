from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class SupportRequestsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def close(self, id: str) -> Any:
        """Fermer une demande d'assistance"""
        path = "/support-requests/{id}/close"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer une demande d'assistance"""
        path = "/support-requests"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Obtenir une demande d'assistance"""
        path = "/support-requests/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les demandes d'assistance"""
        path = "/support-requests"
        return self._request("GET", path, params=params)

