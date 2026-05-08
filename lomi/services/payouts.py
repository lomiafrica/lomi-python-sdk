from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PayoutsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create_wave_payout(self) -> Any:
        """Lancer un virement Wave"""
        path = "/payout/wave"
        return self._request("POST", path)

