
from typing import Optional, Dict, Any, TYPE_CHECKING
from urllib.parse import quote

from .exceptions import LomiError, LomiAuthError, LomiNotFoundError

if TYPE_CHECKING:
    from .client import LomiClient


def _safe_path_param(value: Any) -> str:
    """URL-encode a value for safe interpolation into a URL path segment."""
    return quote(str(value), safe="")


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
    ) -> Any:
        """Make an HTTP request to the merchant API."""
        return self._client._request(method, path, params=params, data=data)
