from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class FinanceService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def get_aging(self) -> Any:
        """Receivables aging buckets"""
        path = "/finance/aging"
        return self._request("GET", path)

    def get_cashflow(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Daily cash in and out over a date range"""
        path = "/finance/cashflow"
        return self._request("GET", path, params=params)

    def get_reconcile(self) -> Any:
        """Reconcile settlements vs transactions vs payouts"""
        path = "/finance/reconcile"
        return self._request("GET", path)

    def get_summary(self) -> Any:
        """Finance summary"""
        path = "/finance/summary"
        return self._request("GET", path)

