from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PayoutMethodsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Add a payout method"""
        path = "/payout-methods"
        return self._request("POST", path)

    def list(self) -> Any:
        """List payout methods"""
        path = "/payout-methods"
        return self._request("GET", path)

