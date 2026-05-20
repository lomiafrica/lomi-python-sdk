from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ChargeService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create_mtn_charge(self) -> Any:
        """Lancer un encaissement direct MTN MoMo"""
        path = "/charge/mtn"
        return self._request("POST", path)

