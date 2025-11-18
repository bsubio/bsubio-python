"""Exception classes for the BSUB.IO SDK."""

from typing import Optional


class BsubError(Exception):
    """Base exception for all BSUB.IO errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


class BsubAuthError(BsubError):
    """Authentication error (401)."""

    def __init__(self, message: str = "Unauthorized: invalid API key"):
        super().__init__(message, 401)


class BsubBadRequestError(BsubError):
    """Bad request error (400)."""

    def __init__(self, message: str):
        super().__init__(message, 400)


class BsubNotFoundError(BsubError):
    """Resource not found error (404)."""

    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404)


class BsubConflictError(BsubError):
    """Conflict error (409)."""

    def __init__(self, message: str):
        super().__init__(message, 409)


class BsubPayloadTooLargeError(BsubError):
    """Payload too large error (413)."""

    def __init__(self, message: str = "File too large"):
        super().__init__(message, 413)
