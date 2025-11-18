"""Data models for the BSUB.IO SDK."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class JobStatus(str, Enum):
    """Job status enumeration."""

    CREATED = "created"
    LOADED = "loaded"
    PENDING = "pending"
    CLAIMED = "claimed"
    PREPARING = "preparing"
    PROCESSING = "processing"
    FINISHED = "finished"
    FAILED = "failed"


@dataclass
class Job:
    """Represents a BSUB.IO job."""

    id: str
    status: JobStatus
    type: str
    user_id: str
    created_at: datetime
    updated_at: datetime
    upload_token: Optional[str] = None
    data_size: Optional[int] = None
    claimed_by: Optional[str] = None
    claimed_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    error_code: Optional[str] = None
    error_message: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Job":
        """Create a Job instance from a dictionary."""
        return cls(
            id=data["id"],
            status=JobStatus(data["status"]),
            type=data["type"],
            user_id=data["user_id"],
            created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            updated_at=datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00")),
            upload_token=data.get("upload_token"),
            data_size=data.get("data_size"),
            claimed_by=data.get("claimed_by"),
            claimed_at=(
                datetime.fromisoformat(data["claimed_at"].replace("Z", "+00:00"))
                if data.get("claimed_at")
                else None
            ),
            finished_at=(
                datetime.fromisoformat(data["finished_at"].replace("Z", "+00:00"))
                if data.get("finished_at")
                else None
            ),
            error_code=data.get("error_code"),
            error_message=data.get("error_message"),
        )

    def is_finished(self) -> bool:
        """Check if the job is finished (successfully or with error)."""
        return self.status in (JobStatus.FINISHED, JobStatus.FAILED)

    def is_successful(self) -> bool:
        """Check if the job finished successfully."""
        return self.status == JobStatus.FINISHED


@dataclass
class ProcessingTypeIO:
    """Input/Output information for a processing type."""

    mime_types: List[str]
    ext: Optional[str] = None
    display: Optional[str] = None


@dataclass
class ProcessingTypeExample:
    """Example usage for a processing type."""

    cmd: str
    desc: str


@dataclass
class ProcessingType:
    """Represents an available processing type."""

    type: str
    name: str
    description: str
    input: ProcessingTypeIO
    output: ProcessingTypeIO
    example: Optional[ProcessingTypeExample] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ProcessingType":
        """Create a ProcessingType instance from a dictionary."""
        input_data = data.get("input", {})
        output_data = data.get("output", {})
        example_data = data.get("example")

        return cls(
            type=data["type"],
            name=data["name"],
            description=data["description"],
            input=ProcessingTypeIO(
                mime_types=input_data.get("mime_in", []),
            ),
            output=ProcessingTypeIO(
                mime_types=output_data.get("mime_out", []),
                ext=output_data.get("ext"),
                display=output_data.get("display"),
            ),
            example=(
                ProcessingTypeExample(
                    cmd=example_data["cmd"],
                    desc=example_data["desc"],
                )
                if example_data
                else None
            ),
        )
