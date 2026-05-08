"""lomi-sdk exceptions."""

from typing import Optional, Any


class LomiError(Exception):
    """Base SDK error."""

    def __init__(self, message: str, status_code: Optional[int] = None, body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class LomiAuthError(LomiError):
    """Invalid API credentials."""


class LomiNotFoundError(LomiError):
    """Resource missing."""
