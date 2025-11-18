"""Main client for the BSUB.IO API."""

import time
from pathlib import Path
from typing import Any, BinaryIO, Dict, List, Optional, Tuple, Union

import requests

from .exceptions import (
    BsubAuthError,
    BsubBadRequestError,
    BsubConflictError,
    BsubError,
    BsubNotFoundError,
    BsubPayloadTooLargeError,
)
from .models import Job, JobStatus, ProcessingType


class BsubClient:
    """Client for interacting with the BSUB.IO API.

    Example:
        >>> client = BsubClient(api_key="your-api-key")
        >>> job = client.create_job("pdf/extract")
        >>> client.upload_file(job.id, job.upload_token, "document.pdf")
        >>> client.submit_job(job.id)
        >>> job = client.wait_for_job(job.id)
        >>> if job.is_successful():
        >>>     output = client.get_output(job.id)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://app.bsub.io",
        timeout: int = 30,
    ):
        """Initialize the BSUB.IO client.

        Args:
            api_key: Your BSUB.IO API key
            base_url: Base URL for the API (default: https://app.bsub.io)
            timeout: Request timeout in seconds (default: 30)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {api_key}",
                "User-Agent": "bsubio-python/1.0.0",
            }
        )

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise appropriate exceptions."""
        if response.status_code == 204:
            return {"success": True}

        try:
            data = response.json()
        except Exception:
            data = {"error": response.text or "Unknown error"}

        if response.status_code == 401:
            raise BsubAuthError(data.get("error", "Unauthorized"))
        elif response.status_code == 400:
            raise BsubBadRequestError(data.get("error", "Bad request"))
        elif response.status_code == 404:
            raise BsubNotFoundError(data.get("error", "Not found"))
        elif response.status_code == 409:
            raise BsubConflictError(data.get("error", "Conflict"))
        elif response.status_code == 413:
            raise BsubPayloadTooLargeError(data.get("error", "Payload too large"))
        elif response.status_code >= 400:
            raise BsubError(
                data.get("error", f"HTTP {response.status_code}"),
                response.status_code,
            )

        return data  # type: ignore[no-any-return]

    def create_job(self, job_type: str) -> Job:
        """Create a new job.

        Args:
            job_type: Processing type (e.g., "pdf/extract"). See get_types() for available types.

        Returns:
            Job: The created job with upload_token for uploading data.

        Raises:
            BsubAuthError: If authentication fails
            BsubBadRequestError: If the request is invalid
        """
        response = self._session.post(
            f"{self.base_url}/v1/jobs",
            json={"type": job_type},
            timeout=self.timeout,
        )
        data = self._handle_response(response)
        return Job.from_dict(data["data"])

    def get_job(self, job_id: str) -> Job:
        """Get job details.

        Args:
            job_id: Job ID (UUID)

        Returns:
            Job: The job details

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
        """
        response = self._session.get(
            f"{self.base_url}/v1/jobs/{job_id}",
            timeout=self.timeout,
        )
        data = self._handle_response(response)
        return Job.from_dict(data["data"])

    def list_jobs(
        self,
        status: Optional[JobStatus] = None,
        limit: int = 20,
    ) -> Tuple[List[Job], int]:
        """List jobs for the authenticated user.

        Args:
            status: Filter by job status (optional)
            limit: Maximum number of jobs to return (default: 20, max: 100)

        Returns:
            tuple[list[Job], int]: A tuple of (jobs list, total count)

        Raises:
            BsubAuthError: If authentication fails
        """
        params: dict[str, Any] = {"limit": limit}
        if status:
            params["status"] = status.value

        response = self._session.get(
            f"{self.base_url}/v1/jobs",
            params=params,
            timeout=self.timeout,
        )
        data = self._handle_response(response)
        jobs = [Job.from_dict(job_data) for job_data in data["data"]["jobs"]]
        total = data["data"]["total"]
        return jobs, total

    def upload_file(
        self,
        job_id: str,
        upload_token: str,
        file_path: Union[str, Path, BinaryIO],
    ) -> int:
        """Upload a file to a job.

        Args:
            job_id: Job ID (UUID)
            upload_token: Upload token from job creation
            file_path: Path to the file or file-like object to upload

        Returns:
            int: Size of the uploaded file in bytes

        Raises:
            BsubAuthError: If the upload token is invalid
            BsubNotFoundError: If the job is not found
            BsubPayloadTooLargeError: If the file is too large
        """
        if isinstance(file_path, (str, Path)):
            with open(file_path, "rb") as f:
                return self._upload_file_handle(job_id, upload_token, f, Path(file_path).name)
        else:
            filename = getattr(file_path, "name", "upload")
            return self._upload_file_handle(job_id, upload_token, file_path, filename)

    def _upload_file_handle(
        self,
        job_id: str,
        upload_token: str,
        file_handle: BinaryIO,
        filename: str,
    ) -> int:
        """Internal method to upload a file handle."""
        # Don't use the session's default auth header for uploads
        headers = {"User-Agent": "bsubio-python/1.0.0"}

        response = requests.post(
            f"{self.base_url}/v1/upload/{job_id}",
            params={"token": upload_token},
            files={"file": (filename, file_handle)},
            headers=headers,
            timeout=self.timeout * 3,  # Longer timeout for uploads
        )
        data = self._handle_response(response)
        return data.get("data_size", 0)  # type: ignore[no-any-return]

    def submit_job(self, job_id: str) -> None:
        """Submit a job for processing.

        Args:
            job_id: Job ID (UUID)

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
            BsubBadRequestError: If the job cannot be submitted
        """
        response = self._session.post(
            f"{self.base_url}/v1/jobs/{job_id}/submit",
            timeout=self.timeout,
        )
        self._handle_response(response)

    def cancel_job(self, job_id: str) -> None:
        """Cancel a pending or in-progress job.

        Args:
            job_id: Job ID (UUID)

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
            BsubBadRequestError: If the job cannot be cancelled
        """
        response = self._session.post(
            f"{self.base_url}/v1/jobs/{job_id}/cancel",
            timeout=self.timeout,
        )
        self._handle_response(response)

    def delete_job(self, job_id: str) -> None:
        """Delete a job and its associated data.

        Only finished or failed jobs can be deleted.

        Args:
            job_id: Job ID (UUID)

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
            BsubConflictError: If the job is still in progress
        """
        response = self._session.delete(
            f"{self.base_url}/v1/jobs/{job_id}",
            timeout=self.timeout,
        )
        self._handle_response(response)

    def get_output(self, job_id: str) -> bytes:
        """Get the output (stdout) of a finished job.

        Args:
            job_id: Job ID (UUID)

        Returns:
            bytes: The job output

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
            BsubConflictError: If the job is not finished yet
        """
        response = self._session.get(
            f"{self.base_url}/v1/jobs/{job_id}/output",
            timeout=self.timeout,
        )
        if response.status_code >= 400:
            self._handle_response(response)
        return response.content

    def get_logs(self, job_id: str) -> str:
        """Get the logs (stderr) of a job.

        Useful for debugging failed jobs.

        Args:
            job_id: Job ID (UUID)

        Returns:
            str: The job logs

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
        """
        response = self._session.get(
            f"{self.base_url}/v1/jobs/{job_id}/logs",
            timeout=self.timeout,
        )
        if response.status_code >= 400:
            self._handle_response(response)
        return response.text

    def wait_for_job(
        self,
        job_id: str,
        poll_interval: float = 2.0,
        timeout: Optional[float] = None,
    ) -> Job:
        """Wait for a job to finish.

        Polls the job status until it reaches a terminal state (finished or failed).

        Args:
            job_id: Job ID (UUID)
            poll_interval: Time to wait between polls in seconds (default: 2.0)
            timeout: Maximum time to wait in seconds (default: None = wait forever)

        Returns:
            Job: The finished job

        Raises:
            BsubAuthError: If authentication fails
            BsubNotFoundError: If the job is not found
            TimeoutError: If the timeout is reached
        """
        start_time = time.time()

        while True:
            job = self.get_job(job_id)

            if job.is_finished():
                return job

            if timeout and (time.time() - start_time) >= timeout:
                raise TimeoutError(f"Job {job_id} did not finish within {timeout} seconds")

            time.sleep(poll_interval)

    def get_types(self) -> List[ProcessingType]:
        """Get available processing types.

        Returns:
            list[ProcessingType]: List of available processing types

        Note:
            This endpoint does not require authentication.
        """
        response = requests.get(
            f"{self.base_url}/v1/types",
            timeout=self.timeout,
        )
        if response.status_code >= 400:
            self._handle_response(response)
        data = response.json()
        return [ProcessingType.from_dict(type_data) for type_data in data["types"]]

    def get_version(self) -> Dict[str, str]:
        """Get API version information.

        Returns:
            dict[str, str]: Version information

        Note:
            This endpoint does not require authentication.
        """
        response = requests.get(
            f"{self.base_url}/v1/version",
            timeout=self.timeout,
        )
        if response.status_code >= 400:
            self._handle_response(response)
        return response.json()  # type: ignore[no-any-return]

    def close(self) -> None:
        """Close the client session."""
        self._session.close()

    def __enter__(self) -> "BsubClient":
        """Context manager entry."""
        return self

    def __exit__(self, *args: Any) -> None:
        """Context manager exit."""
        self.close()
