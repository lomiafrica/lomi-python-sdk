from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class LogsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, id: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Get a log entry"""
        path = "/logs/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path, params=params)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List logs"""
        path = "/logs"
        return self._request("GET", path, params=params)

