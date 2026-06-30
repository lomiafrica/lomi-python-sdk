from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class OrganizationService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get_settings(self) -> Any:
        """Get Radar settings for the organization"""
        path = "/organization/radar-settings"
        return self._request("GET", path)

    def update_settings(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Update Radar settings"""
        path = "/organization/radar-settings"
        return self._request("PATCH", path, data=body)

