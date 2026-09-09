from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class AccountService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def delete_account(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Supprimer le compte marchand"""
        path = "/account/delete"
        return self._request("POST", path, data=body)

    def export(self) -> Any:
        """Exporter les données du compte"""
        path = "/account/export"
        return self._request("POST", path)

