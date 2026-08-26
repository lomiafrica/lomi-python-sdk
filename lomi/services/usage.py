from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class UsageService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def check_entitlement(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Check if a customer has an active entitlement"""
        path = "/usage/entitlements"
        return self._request("GET", path, params=params)

    def create(self) -> Any:
        """Record a usage event"""
        path = "/usage/events"
        return self._request("POST", path)

    def create_entitlement(self) -> Any:
        """Create or update a plan entitlement feature"""
        path = "/usage/entitlements"
        return self._request("POST", path)

    def create_subscription(self) -> Any:
        """Create a usage subscription"""
        path = "/usage/subscriptions"
        return self._request("POST", path)

    def get(self, id: str) -> Any:
        """Get a usage event"""
        path = "/usage/events/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def get_revenue(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Combined MRR + usage + one-time revenue metrics"""
        path = "/usage/revenue"
        return self._request("GET", path, params=params)

    def grant_credits(self) -> Any:
        """Credit prepaid usage units to a customer meter wallet"""
        path = "/usage/credits"
        return self._request("POST", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List usage events"""
        path = "/usage/events"
        return self._request("GET", path, params=params)

    def list_periods(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List usage billing periods"""
        path = "/usage/periods"
        return self._request("GET", path, params=params)

