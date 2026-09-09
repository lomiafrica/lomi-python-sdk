from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class InvoicesService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def create(self) -> Any:
        """Créer une facture"""
        path = "/invoices"
        return self._request("POST", path)

    def create_checkout_session(self, id: str) -> Any:
        """Créer ou récupérer une session de paiement de facture"""
        path = "/invoices/{id}/checkout-session"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def finalize(self, id: str) -> Any:
        """Finalize a draft invoice"""
        path = "/invoices/{id}/finalize"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Obtenir une facture"""
        path = "/invoices/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Lister les factures"""
        path = "/invoices"
        return self._request("GET", path, params=params)

    def pdf(self, id: str) -> Any:
        """Invoice PDF"""
        path = "/invoices/{id}/pdf"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def remind(self, id: str) -> Any:
        """Send an invoice reminder"""
        path = "/invoices/{id}/remind"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def send(self, id: str) -> Any:
        """Send an invoice"""
        path = "/invoices/{id}/send"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

    def update(self, id: str) -> Any:
        """Modifier une facture"""
        path = "/invoices/{id}"
        path = path.replace("{id}", str(id))
        return self._request("PATCH", path)

    def void_invoice(self, id: str) -> Any:
        """Void an invoice"""
        path = "/invoices/{id}/void"
        path = path.replace("{id}", str(id))
        return self._request("POST", path)

