from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ExportsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Create an export job"""
        path = "/exports"
        return self._request("POST", path, data=body)

    def get(self, id: str) -> Any:
        """Get export job status and download URL"""
        path = "/exports/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self) -> Any:
        """List export jobs"""
        path = "/exports"
        return self._request("GET", path)

