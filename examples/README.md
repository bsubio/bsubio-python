# BSUB.IO Python SDK Examples

This directory contains example scripts demonstrating how to use the BSUB.IO Python SDK.

## Setup

1. Install the SDK:
   ```bash
   cd ..
   pip install -e .
   ```

2. Set your API key:
   ```bash
   export BSUBIO_API_KEY=your-api-key-here
   ```

## Examples

### 01_create_job.py
Basic example showing how to create a new job.

```bash
python 01_create_job.py
```

### 02_upload_and_submit.py
Complete workflow showing how to:
- Create a job
- Upload a file
- Submit the job for processing
- Poll for completion

```bash
python 02_upload_and_submit.py
```

### 03_list_jobs.py
Shows how to list and filter jobs.

```bash
python 03_list_jobs.py
```
