from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ProvidersService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List payment providers"""
        path = "/providers"
        return self._request("GET", path, params=params)

