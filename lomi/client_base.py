
from typing import Optional, Dict, Any, List, Type, TypeVar, TYPE_CHECKING
import requests
from .exceptions import LomiError, LomiAuthError, LomiNotFoundError
from pydantic import BaseModel

if TYPE_CHECKING:
    from .client import LomiClient

T = TypeVar("T", bound=BaseModel)

class ClientBase:
    def __init__(self, client: 'LomiClient'):
        self._client = client

    def _request(self, method: str, path: str, model: Type[T] = None, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Any:
        return self._client._request(method, path, model, params, data)
