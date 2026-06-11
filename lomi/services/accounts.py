from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class AccountsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def check_balance(self, currency: str) -> Any:
        """Vérifier le solde disponible"""
        path = "/accounts/balance/check/{currency}"
        path = path.replace("{currency}", str(currency))
        return self._request("GET", path)

    def get_balance(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Solde du compte"""
        path = "/accounts/balance"
        return self._request("GET", path, params=params)

    def get_balance_breakdown(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Détail du solde"""
        path = "/accounts/balance/breakdown"
        return self._request("GET", path, params=params)

