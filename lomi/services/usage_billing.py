from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class UsageBillingService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def check_entitlement(self) -> Any:
        """Check if a customer has an active entitlement"""
        path = "/usage-billing/entitlements/check"
        return self._request("GET", path)

    def create_entitlement(self) -> Any:
        """Create or update a plan entitlement feature"""
        path = "/usage-billing/entitlements"
        return self._request("POST", path)

    def get_revenue(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """Combined MRR + usage + one-time revenue metrics"""
        path = "/usage-billing/revenue"
        return self._request("GET", path, params=params)

    def get_subscription_usage(self, subscriptionId: str) -> Any:
        """Get meter usage for a subscription"""
        path = "/usage-billing/subscriptions/{subscriptionId}/usage"
        path = path.replace("{subscriptionId}", str(subscriptionId))
        return self._request("GET", path)

    def grant_credits(self) -> Any:
        """Credit prepaid usage units to a customer meter wallet"""
        path = "/usage-billing/credits"
        return self._request("POST", path)

    def list_periods(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List usage billing periods"""
        path = "/usage-billing/periods"
        return self._request("GET", path, params=params)

