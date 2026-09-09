from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class CouponsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Créer un coupon"""
        path = "/coupons"
        return self._request("POST", path)

    def delete(self, id: str) -> Any:
        """Supprimer un coupon"""
        path = "/coupons/{id}"
        path = path.replace("{id}", str(id))
        return self._request("DELETE", path)

    def get(self, id: str) -> Any:
        """Obtenir un coupon par ID"""
        path = "/coupons/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_performance(self, id: str) -> Any:
        """Indicateurs de performance du coupon"""
        path = "/coupons/{id}/performance"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self) -> Any:
        """Lister les coupons"""
        path = "/coupons"
        return self._request("GET", path)

