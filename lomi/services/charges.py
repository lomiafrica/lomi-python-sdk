from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class ChargesService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def cancel_card_charge(self, id: str) -> Any:
        """Annuler un encaissement carte"""
        path = "/charge/card/{id}/cancel"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def create_card_charge(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un encaissement carte (client_secret)"""
        path = "/charge/card"
        return self._request("POST", path, data=body)

    def create_mtn_charge(self) -> Any:
        """Lancer un encaissement direct MTN MoMo"""
        path = "/charge/mtn"
        return self._request("POST", path)

    def create_wave_charge(self) -> Any:
        """Lancer un encaissement direct Wave"""
        path = "/charge/wave"
        return self._request("POST", path)

    def get_card_charge(self, id: str) -> Any:
        """Obtenir un encaissement carte"""
        path = "/charge/card/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

