"""
BSUB.IO Python SDK

A Python client library for the BSUB.IO API - batch processing for compute-intensive workloads.
Perfect for PDF processing, video transcoding, audio transcription, and more.
"""

from .client import BsubClient
from .exceptions import (
    BsubAuthError,
    BsubBadRequestError,
    BsubError,
    BsubNotFoundError,
)
from .models import Job, JobStatus, ProcessingType

__version__ = "1.0.0"
__all__ = [
    "BsubClient",
    "Job",
    "JobStatus",
    "ProcessingType",
    "BsubError",
    "BsubAuthError",
    "BsubNotFoundError",
    "BsubBadRequestError",
]
