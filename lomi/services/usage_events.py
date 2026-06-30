from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class UsageEventsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Record a usage event"""
        path = "/usage-events"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Get a usage event"""
        path = "/usage-events/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List usage events"""
        path = "/usage-events"
        return self._request("GET", path, params=params)

