from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class SettingsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get_checkout(self) -> Any:
        """Lire les réglages checkout"""
        path = "/settings/checkout"
        return self._request("GET", path)

    def get_storefront(self) -> Any:
        """Lire la vitrine"""
        path = "/settings/storefront"
        return self._request("GET", path)

    def update_checkout(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Mettre à jour les réglages checkout"""
        path = "/settings/checkout"
        return self._request("PATCH", path, data=body)

    def update_storefront(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Mettre à jour la vitrine"""
        path = "/settings/storefront"
        return self._request("PATCH", path, data=body)

