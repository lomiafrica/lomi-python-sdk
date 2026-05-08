from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ChargesService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create_wave_charge(self) -> Any:
        """Lancer un encaissement direct Wave"""
        path = "/charge/wave"
        return self._request("POST", path)

