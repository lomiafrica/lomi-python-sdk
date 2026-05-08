"""Types are dictated by the public API OpenAPI schema; use Dict[str, Any] or narrow in your app."""
from typing import Any, Dict

__all__ = ["JSONDict"]
JSONDict = Dict[str, Any]
