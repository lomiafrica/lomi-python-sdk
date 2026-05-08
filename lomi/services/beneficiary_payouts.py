from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class BeneficiaryPayoutsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Lancer un paiement vers un bénéficiaire"""
        path = "/beneficiary-payouts"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Obtenir un paiement bénéficiaire par ID"""
        path = "/beneficiary-payouts/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les paiements vers bénéficiaires"""
        path = "/beneficiary-payouts"
        return self._request("GET", path, params=params)

