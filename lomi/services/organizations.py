from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class OrganizationsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str) -> Any:
        """Organisation par ID"""
        path = "/organizations/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_metrics(self) -> Any:
        """Indicateurs de l'organisation"""
        path = "/organizations/metrics"
        return self._request("GET", path)

    def list(self) -> Any:
        """Détails de l'organisation"""
        path = "/organizations"
        return self._request("GET", path)

