"""Tests for data models."""

from datetime import datetime

from bsubio.models import Job, JobStatus, ProcessingType


class TestJob:
    """Tests for Job model."""

    def test_job_from_dict(self) -> None:
        """Test creating a job from dictionary."""
        data = {
            "id": "test-id",
            "status": "finished",
            "type": "pdf/extract",
            "user_id": "user123",
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-15T10:35:00Z",
            "finished_at": "2024-01-15T10:35:00Z",
        }

        job = Job.from_dict(data)

        assert job.id == "test-id"
        assert job.status == JobStatus.FINISHED
        assert job.type == "pdf/extract"
        assert isinstance(job.created_at, datetime)
        assert isinstance(job.finished_at, datetime)

    def test_job_is_finished(self) -> None:
        """Test is_finished method."""
        finished_job = Job(
            id="test",
            status=JobStatus.FINISHED,
            type="test",
            user_id="user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        assert finished_job.is_finished()

        pending_job = Job(
            id="test",
            status=JobStatus.PENDING,
            type="test",
            user_id="user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        assert not pending_job.is_finished()

    def test_job_is_successful(self) -> None:
        """Test is_successful method."""
        successful_job = Job(
            id="test",
            status=JobStatus.FINISHED,
            type="test",
            user_id="user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        assert successful_job.is_successful()

        failed_job = Job(
            id="test",
            status=JobStatus.FAILED,
            type="test",
            user_id="user",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        assert not failed_job.is_successful()


class TestProcessingType:
    """Tests for ProcessingType model."""

    def test_processing_type_from_dict(self) -> None:
        """Test creating a processing type from dictionary."""
        data = {
            "type": "pdf/extract",
            "name": "PDF Extraction",
            "description": "Extract text from PDF",
            "input": {"mime_in": ["application/pdf"]},
            "output": {
                "mime_out": ["text/plain"],
                "ext": ".txt",
                "display": "text",
            },
            "example": {
                "cmd": "bsubio submit pdf/extract doc.pdf",
                "desc": "Extract text from PDF",
            },
        }

        proc_type = ProcessingType.from_dict(data)

        assert proc_type.type == "pdf/extract"
        assert proc_type.name == "PDF Extraction"
        assert proc_type.input.mime_types == ["application/pdf"]
        assert proc_type.output.ext == ".txt"
        assert proc_type.example is not None
        assert proc_type.example.cmd == "bsubio submit pdf/extract doc.pdf"
