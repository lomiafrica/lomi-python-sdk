from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class PaymentIntentsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Créer un Payment Intent carte (client_secret)"""
        path = "/payment-intents"
        return self._request("POST", path, data=body)

