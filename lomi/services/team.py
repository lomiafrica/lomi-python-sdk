from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class TeamService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def invite(self, body: Optional[Dict[str, Any]] = None) -> Any:
        """Inviter un membre"""
        path = "/team/invitations"
        return self._request("POST", path, data=body)

    def list(self) -> Any:
        """Lister l’équipe"""
        path = "/team"
        return self._request("GET", path)

    def list_roles(self) -> Any:
        """Lister les rôles"""
        path = "/team/roles"
        return self._request("GET", path)

    def remove(self, memberId: str) -> Any:
        """Retirer un membre"""
        path = "/team/members/{memberId}"
        path = path.replace("{memberId}", str(memberId))
        return self._request("DELETE", path)

    def revoke_invite(self) -> Any:
        """Révoquer une invitation"""
        path = "/team/invitations"
        return self._request("DELETE", path)

    def update_role(self, memberId: str, body: Optional[Dict[str, Any]] = None) -> Any:
        """Changer le rôle d’un membre"""
        path = "/team/members/{memberId}"
        path = path.replace("{memberId}", str(memberId))
        return self._request("PATCH", path, data=body)

