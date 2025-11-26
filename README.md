# bsubio-python

> Python SDK for [bsub.io](https://bsub.io) — zero-setup batch execution for compute-intensive workloads.

**No infrastructure management. No setup headaches. Just submit your files and retrieve results.**

Perfect for:
- 📄 **PDF extraction** — pull text and data from documents
- 🎬 **Video transcoding** — convert media formats at scale
- 🎤 **Audio transcription** — speech to text
- 🖼️ **Image processing** — resize, convert, optimize
- ...and any other compute-heavy tasks you can throw at it!

## Quick Start

### Installation

```bash
pip install bsubio
```

That's it! No infrastructure to configure, no servers to manage.

### Basic Usage

```python
import os
import bsubio

# Configure with your API key (grab it from https://app.bsub.io)
config = bsubio.Configuration(
    access_token=os.environ["BSUB_API_KEY"]
)

# Create a client and start submitting jobs!
with bsubio.ApiClient(config) as client:
    jobs_api = bsubio.JobsApi(client)

    # Create a job
    job = jobs_api.create_job({
        "type": "pdf-extract",
        "name": "Extract invoice data"
    })

    # Upload your file
    jobs_api.upload_job_data(job.id, file=open("invoice.pdf", "rb"))

    # Submit for processing
    jobs_api.submit_job(job.id)

    # Check status
    status = jobs_api.get_job(job.id)
    print(f"Job status: {status.state}")

    # Get results when ready
    if status.state == "finished":
        output = jobs_api.get_job_output(job.id)
        print(output)
```

**That's the entire workflow.** Create → Upload → Submit → Retrieve. No queues to manage, no workers to provision.

## How It Works

bsub.io handles the heavy lifting:

1. **Create** a job with `POST /v1/jobs` — get back a job ID and upload token
2. **Upload** your data with `POST /v1/upload/{jobId}` — send files for processing
3. **Submit** for processing with `POST /v1/jobs/{jobId}/submit` — kick off the work
4. **Monitor** status with `GET /v1/jobs/{jobId}` — track progress
5. **Retrieve** results with `GET /v1/jobs/{jobId}/output` — get your output

### Job States

Your job progresses through these states:
- `created` → Job created, awaiting upload
- `loaded` → Data uploaded successfully
- `pending` → Waiting in queue
- `processing` → Work in progress
- `finished` → All done!
- `failed` → Something went wrong (check logs)

## Authentication

Get your API key from the [bsub.io dashboard](https://app.bsub.io) and pass it as a Bearer token:

```python
config = bsubio.Configuration(
    access_token="your-api-key-here"
)
```

## Requirements

- Python 3.9+
- That's it!

## API Reference

All URIs are relative to `https://app.bsub.io`

### Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JobsApi* | [**cancel_job**](docs/JobsApi.md#cancel_job) | **POST** /v1/jobs/{jobId}/cancel | Cancel a job
*JobsApi* | [**create_job**](docs/JobsApi.md#create_job) | **POST** /v1/jobs | Create a new job
*JobsApi* | [**delete_job**](docs/JobsApi.md#delete_job) | **DELETE** /v1/jobs/{jobId} | Delete a job
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /v1/jobs/{jobId} | Get job details
*JobsApi* | [**list_jobs**](docs/JobsApi.md#list_jobs) | **GET** /v1/jobs | List jobs
*JobsApi* | [**submit_job**](docs/JobsApi.md#submit_job) | **POST** /v1/jobs/{jobId}/submit | Submit job for processing
*JobsApi* | [**upload_job_data**](docs/JobsApi.md#upload_job_data) | **POST** /v1/upload/{jobId} | Upload data to a job
*OutputApi* | [**get_job_logs**](docs/OutputApi.md#get_job_logs) | **GET** /v1/jobs/{jobId}/logs | Get job logs (stderr)
*OutputApi* | [**get_job_output**](docs/OutputApi.md#get_job_output) | **GET** /v1/jobs/{jobId}/output | Get job output (stdout)
*SystemApi* | [**get_types**](docs/SystemApi.md#get_types) | **GET** /v1/types | Get available processing types
*SystemApi* | [**get_version**](docs/SystemApi.md#get_version) | **GET** /v1/version | Get API version


### Models

 - [CancelJob200Response](docs/CancelJob200Response.md)
 - [CreateJob201Response](docs/CreateJob201Response.md)
 - [CreateJobRequest](docs/CreateJobRequest.md)
 - [Error](docs/Error.md)
 - [GetTypes200Response](docs/GetTypes200Response.md)
 - [GetVersion200Response](docs/GetVersion200Response.md)
 - [Job](docs/Job.md)
 - [ListJobs200Response](docs/ListJobs200Response.md)
 - [ListJobs200ResponseData](docs/ListJobs200ResponseData.md)
 - [ProcessingType](docs/ProcessingType.md)
 - [ProcessingTypeExample](docs/ProcessingTypeExample.md)
 - [ProcessingTypeInput](docs/ProcessingTypeInput.md)
 - [ProcessingTypeOutput](docs/ProcessingTypeOutput.md)
 - [SubmitJob200Response](docs/SubmitJob200Response.md)
 - [UploadJobData200Response](docs/UploadJobData200Response.md)

## Additional Info

### Generated SDK

This Python SDK is automatically generated from the [bsub.io OpenAPI spec](https://app.bsub.io/static/openapi.yaml) using [OpenAPI Generator](https://openapi-generator.tech).

- API version: 1.0.0
- Package version: 1.0.0
- Build package: `org.openapitools.codegen.languages.PythonClientCodegen`

### Development

Want to run tests?

```bash
pytest
```

Alternative installation from source:

```bash
pip install git+https://github.com/bsubio/bsubio-python.git
```

## Get Help

- **Documentation:** [https://bsub.io/docs](https://bsub.io/docs)
- **API Reference:** [https://app.bsub.io/docs](https://app.bsub.io/docs)
- **Issues:** [github.com/bsubio/bsubio-python/issues](https://github.com/bsubio/bsubio-python/issues)

## Author

**Adam Koszek**
Email: contact@bsub.io
Web: [bsub.io](https://bsub.io)




