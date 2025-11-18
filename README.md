# BSUB.IO Python SDK

[![PyPI version](https://badge.fury.io/py/bsubio.svg)](https://badge.fury.io/py/bsubio)
[![Python versions](https://img.shields.io/pypi/pyversions/bsubio.svg)](https://pypi.org/project/bsubio/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for [BSUB.IO](https://bsub.io) - Batch processing for compute-intensive workloads.

Perfect for PDF processing, video transcoding, audio transcription, and more.

## Features

- 🚀 **Simple API** - Easy-to-use client with intuitive methods
- 🔒 **Type Safe** - Full type hints and mypy support
- ⚡ **Async Ready** - Supports concurrent job processing
- 🧪 **Well Tested** - Comprehensive test coverage
- 📦 **Zero Config** - Works out of the box
- 🎯 **Production Ready** - Battle-tested and reliable

## Installation

```bash
pip install bsubio
```

## Quick Start

```python
from bsubio import BsubClient

# Initialize client with your API key
client = BsubClient(api_key="your-api-key")

# Create a job
job = client.create_job("pdf/extract")

# Upload your file
client.upload_file(job.id, job.upload_token, "document.pdf")

# Submit for processing
client.submit_job(job.id)

# Wait for completion
job = client.wait_for_job(job.id)

# Get the results
if job.is_successful():
    output = client.get_output(job.id)
    print(output.decode('utf-8'))
else:
    print(f"Job failed: {job.error_message}")
```

## Usage

### Get Your API Key

Get your API key from the [BSUB.IO Dashboard](https://app.bsub.io).

### Initialize the Client

```python
from bsubio import BsubClient

client = BsubClient(api_key="your-api-key")
```

### Context Manager

The client can be used as a context manager for automatic cleanup:

```python
with BsubClient(api_key="your-api-key") as client:
    # Your code here
    job = client.create_job("passthru")
    # ... rest of your code
# Client automatically closed
```

### Available Processing Types

Get a list of all available processing types:

```python
types = client.get_types()
for proc_type in types:
    print(f"{proc_type.name} ({proc_type.type})")
    print(f"  {proc_type.description}")
```

### Create and Process a Job

```python
# Create a job
job = client.create_job("pdf/extract")
print(f"Job ID: {job.id}")
print(f"Status: {job.status.value}")

# Upload file
client.upload_file(job.id, job.upload_token, "document.pdf")

# Or upload from a file-like object
with open("document.pdf", "rb") as f:
    client.upload_file(job.id, job.upload_token, f)

# Submit for processing
client.submit_job(job.id)

# Wait for completion (with timeout)
job = client.wait_for_job(job.id, poll_interval=2.0, timeout=300.0)

# Check result
if job.is_successful():
    output = client.get_output(job.id)
    # Process output...
else:
    # Get error details
    logs = client.get_logs(job.id)
    print(f"Error: {job.error_message}")
    print(f"Logs: {logs}")
```

### List Jobs

```python
from bsubio import JobStatus

# List all jobs
jobs, total = client.list_jobs(limit=20)
print(f"Total jobs: {total}")

# Filter by status
jobs, total = client.list_jobs(status=JobStatus.FINISHED, limit=10)
for job in jobs:
    print(f"{job.id}: {job.status.value}")
```

### Cancel and Delete Jobs

```python
# Cancel a running job
client.cancel_job(job_id)

# Delete a finished job
client.delete_job(job_id)
```

### Error Handling

```python
from bsubio import BsubClient
from bsubio.exceptions import (
    BsubError,
    BsubAuthError,
    BsubNotFoundError,
    BsubBadRequestError,
)

try:
    job = client.create_job("invalid-type")
except BsubAuthError:
    print("Invalid API key")
except BsubBadRequestError as e:
    print(f"Bad request: {e.message}")
except BsubNotFoundError:
    print("Resource not found")
except BsubError as e:
    print(f"BSUB.IO error: {e.message} (status: {e.status_code})")
```

## Examples

The `examples/` directory contains several complete examples:

- **basic.py** - Simple end-to-end workflow
- **comprehensive.py** - Showcases all SDK features
- **batch.py** - Process multiple files in parallel

Run examples:

```bash
# Set your API key
export BSUB_API_KEY="your-api-key"

# Run an example
python examples/basic.py
```

Or use the Makefile:

```bash
make example NAME=basic
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/bsubio/bsubio-python.git
cd bsubio-python

# Set up development environment
make dev

# Activate virtual environment
source .venv/bin/activate
```

### Run Tests

```bash
make test
```

### Code Quality

```bash
# Format code
make fmt

# Lint code
make lint

# Type check
make typecheck

# Run all checks
make check
```

### Build and Publish

```bash
# Build distribution packages
make build

# Publish to PyPI (requires credentials)
make publish

# Or publish to Test PyPI first
make publish-test
```

## API Reference

### BsubClient

Main client class for interacting with the BSUB.IO API.

#### Methods

- `create_job(job_type: str) -> Job` - Create a new job
- `get_job(job_id: str) -> Job` - Get job details
- `list_jobs(status: JobStatus | None = None, limit: int = 20) -> tuple[list[Job], int]` - List jobs
- `upload_file(job_id: str, upload_token: str, file_path: str | Path | BinaryIO) -> int` - Upload file
- `submit_job(job_id: str) -> None` - Submit job for processing
- `cancel_job(job_id: str) -> None` - Cancel a job
- `delete_job(job_id: str) -> None` - Delete a job
- `get_output(job_id: str) -> bytes` - Get job output
- `get_logs(job_id: str) -> str` - Get job logs
- `wait_for_job(job_id: str, poll_interval: float = 2.0, timeout: float | None = None) -> Job` - Wait for job completion
- `get_types() -> list[ProcessingType]` - Get available processing types
- `get_version() -> dict[str, str]` - Get API version

### Models

#### Job

Represents a BSUB.IO job with properties:
- `id: str` - Job ID (UUID)
- `status: JobStatus` - Current status
- `type: str` - Processing type
- `user_id: str` - Owner user ID
- `upload_token: str | None` - Upload token (only in created state)
- `data_size: int | None` - Size of uploaded data
- `created_at: datetime` - Creation timestamp
- `updated_at: datetime` - Last update timestamp
- `finished_at: datetime | None` - Completion timestamp
- `error_message: str | None` - Error message if failed

Methods:
- `is_finished() -> bool` - Check if job is finished
- `is_successful() -> bool` - Check if job completed successfully

#### JobStatus

Enum of job statuses:
- `CREATED` - Job created, awaiting upload
- `LOADED` - Data uploaded
- `PENDING` - Waiting in queue
- `CLAIMED` - Worker claimed the job
- `PREPARING` - Worker preparing
- `PROCESSING` - Processing in progress
- `FINISHED` - Completed successfully
- `FAILED` - Processing failed

#### ProcessingType

Represents an available processing type with properties:
- `type: str` - Type identifier
- `name: str` - Human-readable name
- `description: str` - Description
- `input: ProcessingTypeIO` - Input format info
- `output: ProcessingTypeIO` - Output format info
- `example: ProcessingTypeExample | None` - Example usage

## Requirements

- Python 3.9 or higher
- requests >= 2.31.0

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Links

- **Website:** [https://bsub.io](https://bsub.io)
- **Documentation:** [https://bsub.io/docs](https://bsub.io/docs)
- **Dashboard:** [https://app.bsub.io](https://app.bsub.io)
- **GitHub:** [https://github.com/bsubio/bsubio-python](https://github.com/bsubio/bsubio-python)
- **PyPI:** [https://pypi.org/project/bsubio/](https://pypi.org/project/bsubio/)

## Support

For issues and questions:
- Open an issue on [GitHub](https://github.com/bsubio/bsubio-python/issues)
- Contact support at [support@bsub.io](mailto:support@bsub.io)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
