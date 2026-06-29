from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class ProductsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def add_price(self, id: str) -> Any:
        """Ajouter un prix à un produit"""
        path = "/products/{id}/prices"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("POST", path)

    def create(self) -> Any:
        """Créer un produit"""
        path = "/products"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Obtenir un produit par ID"""
        path = "/products/{id}"
        path = path.replace("{id}", _safe_path_param(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les produits"""
        path = "/products"
        return self._request("GET", path, params=params)

    def set_default_price(self, id: str, priceId: str) -> Any:
        """Définir le prix par défaut"""
        path = "/products/{id}/prices/{priceId}/set-default"
        path = path.replace("{id}", _safe_path_param(id))
        path = path.replace("{priceId}", _safe_path_param(priceId))
        return self._request("POST", path)

