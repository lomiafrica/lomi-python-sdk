from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class LogsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get(self, type: str, id: str) -> Any:
        """Get a log entry"""
        path = "/logs/{type}/{id}"
        path = path.replace("{type}", str(type))
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List logs"""
        path = "/logs"
        return self._request("GET", path, params=params)

