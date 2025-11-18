"""Pytest configuration and fixtures."""

import pytest

from bsubio import BsubClient


@pytest.fixture
def api_key() -> str:
    """Return a test API key."""
    return "test_api_key_12345"


@pytest.fixture
def client(api_key: str) -> BsubClient:
    """Return a test client instance."""
    return BsubClient(api_key=api_key, base_url="https://app.bsub.io")


@pytest.fixture
def mock_job_data() -> dict:
    """Return mock job data for testing."""
    return {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "status": "created",
        "type": "pdf/extract",
        "user_id": "user123",
        "upload_token": "tok_abc123",
        "data_size": None,
        "claimed_by": None,
        "claimed_at": None,
        "finished_at": None,
        "error_code": None,
        "error_message": None,
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z",
    }
