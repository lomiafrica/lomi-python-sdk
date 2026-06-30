from __future__ import annotations

from typing import Any, Dict, Optional

from ..client_base import ClientBase


class RiskAssessmentsService(ClientBase):
    """Public merchant API — generated from OpenAPI allowlist."""

    def find_one(self, id: str) -> Any:
        """Get a risk assessment"""
        path = "/risk-assessments/{id}"
        path = path.replace("{id}", str(id))
        return self._request("GET", path)

    def list_assessments(self, params: Optional[Dict[str, Any]] = None) -> Any:
        """List payment risk assessments"""
        path = "/risk-assessments"
        return self._request("GET", path, params=params)

