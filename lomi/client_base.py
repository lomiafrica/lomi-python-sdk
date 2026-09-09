
from typing import Optional, Dict, Any, TYPE_CHECKING
import warnings
import requests

from .exceptions import LomiError, LomiAuthError, LomiNotFoundError

if TYPE_CHECKING:
    from .client import LomiClient


class ClientBase:
    """HTTP helpers shared by generated services."""

    def __init__(self, client: "LomiClient"):
        self._client = client

    def _request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        account: Optional[str] = None,
        idempotency_key: Optional[str] = None,
    ) -> Any:
        """Make an HTTP request to the merchant API.

        account= overrides the client-level Lomi-Account for this call
        ("" sends no Lomi-Account header at all).
        """
        return self._client._request(
            method,
            path,
            params=params,
            data=data,
            account=account,
            idempotency_key=idempotency_key,
        )
