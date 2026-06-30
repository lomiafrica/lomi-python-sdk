from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase, _safe_path_param


class CustomerSubscriptionsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def delete(self, subscription_id: str) -> Any:
        """Cancel customer subscription"""
        path = "/customer-subscriptions/{subscription_id}"
        path = path.replace("{subscription_id}", _safe_path_param(subscription_id))
        return self._request("DELETE", path)

    def get(self, subscription_id: str) -> Any:
        """Get customer subscription"""
        path = "/customer-subscriptions/{subscription_id}"
        path = path.replace("{subscription_id}", _safe_path_param(subscription_id))
        return self._request("GET", path)

    def list(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List customer subscriptions"""
        path = "/customer-subscriptions"
        return self._request("GET", path, params=params)

    def update(self, subscription_id: str) -> Any:
        """Update customer subscription"""
        path = "/customer-subscriptions/{subscription_id}"
        path = path.replace("{subscription_id}", _safe_path_param(subscription_id))
        return self._request("PATCH", path)

