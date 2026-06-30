from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ChargesService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def cancel_card_charge(self, id: str) -> Any:
        """Cancel card charge"""
        path = "/charge/card/{id}/cancel"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def create_card_charge(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Create card charge (client_secret)"""
        path = "/charge/card"
        return self._request("POST", path, data=body)

    def create_mtn_charge(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Create MTN MoMo charge"""
        path = "/charge/mtn"
        return self._request("POST", path, data=body)

    def create_switch_charge(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Create Switch charge (server-side card authorization)"""
        path = "/charge/switch"
        return self._request("POST", path, data=body)

    def create_wave_charge(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Create direct Wave charge"""
        path = "/charge/wave"
        return self._request("POST", path, data=body)

    def get_card_charge(self, id: str) -> Any:
        """Retrieve card charge"""
        path = "/charge/card/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

