from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PayoutService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create_spi_payout(self) -> Any:
        """Lancer un virement SPI"""
        path = "/payout/spi"
        return self._request("POST", path)

