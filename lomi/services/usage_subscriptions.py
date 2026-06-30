from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class UsageSubscriptionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Create a usage subscription"""
        path = "/usage-subscriptions"
        return self._request("POST", path)

