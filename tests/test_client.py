"""Tests for the BsubClient class."""

from io import BytesIO
from unittest.mock import Mock, mock_open, patch

import pytest

from bsubio import BsubClient, JobStatus
from bsubio.exceptions import (
    BsubAuthError,
    BsubBadRequestError,
    BsubNotFoundError,
)


class TestBsubClient:
    """Tests for BsubClient."""

    def test_client_initialization(self, api_key: str) -> None:
        """Test client initialization."""
        client = BsubClient(api_key=api_key)
        assert client.api_key == api_key
        assert client.base_url == "https://app.bsub.io"
        assert client.timeout == 30

    def test_client_with_custom_base_url(self, api_key: str) -> None:
        """Test client with custom base URL."""
        client = BsubClient(api_key=api_key, base_url="http://localhost:9986")
        assert client.base_url == "http://localhost:9986"

    @patch("bsubio.client.requests.Session.post")
    def test_create_job(self, mock_post: Mock, client: BsubClient, mock_job_data: dict) -> None:
        """Test creating a job."""
        mock_response = Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"success": True, "data": mock_job_data}
        mock_post.return_value = mock_response

        job = client.create_job("pdf/extract")

        assert job.id == mock_job_data["id"]
        assert job.status == JobStatus.CREATED
        assert job.type == "pdf/extract"
        assert job.upload_token == "tok_abc123"
        mock_post.assert_called_once()

    @patch("bsubio.client.requests.Session.get")
    def test_get_job(self, mock_get: Mock, client: BsubClient, mock_job_data: dict) -> None:
        """Test getting job details."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "data": mock_job_data}
        mock_get.return_value = mock_response

        job = client.get_job(mock_job_data["id"])

        assert job.id == mock_job_data["id"]
        assert job.status == JobStatus.CREATED
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.Session.get")
    def test_list_jobs(self, mock_get: Mock, client: BsubClient, mock_job_data: dict) -> None:
        """Test listing jobs."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "data": {"jobs": [mock_job_data], "total": 1},
        }
        mock_get.return_value = mock_response

        jobs, total = client.list_jobs(status=JobStatus.CREATED, limit=10)

        assert len(jobs) == 1
        assert total == 1
        assert jobs[0].id == mock_job_data["id"]
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.post")
    def test_upload_file_with_path(self, mock_post: Mock, client: BsubClient) -> None:
        """Test uploading a file by path."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "File uploaded",
            "data_size": 1024,
        }
        mock_post.return_value = mock_response

        with patch("builtins.open", mock_open(read_data=b"test data")):
            size = client.upload_file("job123", "token123", "/tmp/test.pdf")

        assert size == 1024
        mock_post.assert_called_once()

    @patch("bsubio.client.requests.post")
    def test_upload_file_with_bytes_io(self, mock_post: Mock, client: BsubClient) -> None:
        """Test uploading a file from BytesIO."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "File uploaded",
            "data_size": 9,
        }
        mock_post.return_value = mock_response

        file_obj = BytesIO(b"test data")
        size = client.upload_file("job123", "token123", file_obj)

        assert size == 9
        mock_post.assert_called_once()

    @patch("bsubio.client.requests.Session.post")
    def test_submit_job(self, mock_post: Mock, client: BsubClient) -> None:
        """Test submitting a job."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "message": "Job submitted",
        }
        mock_post.return_value = mock_response

        client.submit_job("job123")

        mock_post.assert_called_once()

    @patch("bsubio.client.requests.Session.delete")
    def test_delete_job(self, mock_delete: Mock, client: BsubClient) -> None:
        """Test deleting a job."""
        mock_response = Mock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        client.delete_job("job123")

        mock_delete.assert_called_once()

    @patch("bsubio.client.requests.Session.get")
    def test_get_output(self, mock_get: Mock, client: BsubClient) -> None:
        """Test getting job output."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"output data"
        mock_get.return_value = mock_response

        output = client.get_output("job123")

        assert output == b"output data"
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.Session.get")
    def test_get_logs(self, mock_get: Mock, client: BsubClient) -> None:
        """Test getting job logs."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "log data"
        mock_get.return_value = mock_response

        logs = client.get_logs("job123")

        assert logs == "log data"
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.get")
    def test_get_types(self, mock_get: Mock, client: BsubClient) -> None:
        """Test getting processing types."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "types": [
                {
                    "type": "pdf/extract",
                    "name": "PDF Text Extraction",
                    "description": "Extract text from PDF",
                    "input": {"mime_in": ["application/pdf"]},
                    "output": {"mime_out": ["text/plain"], "ext": ".txt", "display": "text"},
                }
            ]
        }
        mock_get.return_value = mock_response

        types = client.get_types()

        assert len(types) == 1
        assert types[0].type == "pdf/extract"
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.get")
    def test_get_version(self, mock_get: Mock, client: BsubClient) -> None:
        """Test getting API version."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "version": "1.0.0",
            "server": "bsub.io",
            "build": "2024-01-15T10:30:00Z",
        }
        mock_get.return_value = mock_response

        version = client.get_version()

        assert version["version"] == "1.0.0"
        mock_get.assert_called_once()

    @patch("bsubio.client.requests.Session.get")
    def test_auth_error(self, mock_get: Mock, client: BsubClient) -> None:
        """Test authentication error handling."""
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"success": False, "error": "Unauthorized"}
        mock_get.return_value = mock_response

        with pytest.raises(BsubAuthError):
            client.get_job("job123")

    @patch("bsubio.client.requests.Session.get")
    def test_not_found_error(self, mock_get: Mock, client: BsubClient) -> None:
        """Test not found error handling."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"success": False, "error": "Job not found"}
        mock_get.return_value = mock_response

        with pytest.raises(BsubNotFoundError):
            client.get_job("nonexistent")

    @patch("bsubio.client.requests.Session.post")
    def test_bad_request_error(self, mock_post: Mock, client: BsubClient) -> None:
        """Test bad request error handling."""
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"success": False, "error": "Invalid type"}
        mock_post.return_value = mock_response

        with pytest.raises(BsubBadRequestError):
            client.create_job("")

    def test_context_manager(self, api_key: str) -> None:
        """Test using client as context manager."""
        with BsubClient(api_key=api_key) as client:
            assert client.api_key == api_key
        # Client should be closed after exiting context
