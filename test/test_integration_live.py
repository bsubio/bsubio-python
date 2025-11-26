import json
import os
import time
from pathlib import Path
from uuid import uuid4

import pytest

from bsubio import (
    ApiClient,
    ApiException,
    Configuration,
    CreateJobRequest,
    JobsApi,
    OutputApi,
    SystemApi,
)


def _require_live_config() -> Configuration:
    api_key = os.getenv("BSUB_API_KEY")
    base_url = os.getenv("BSUB_BASE_URL")

    if not api_key and os.getenv("BSUB_TEST_USE_CONFIG"):
        cfg_path = Path.home() / ".config" / "bsubio" / "config.json"
        if cfg_path.exists():
            try:
                data = json.loads(cfg_path.read_text())
                api_key = data.get("api_key") or api_key
                base_url = data.get("base_url") or base_url
            except json.JSONDecodeError:
                pytest.skip(f"Failed to parse config file at {cfg_path}")

    if not api_key:
        pytest.skip("BSUB_API_KEY not set; live integration tests skipped.")

    cfg = Configuration(host=base_url) if base_url else Configuration()
    cfg.access_token = api_key
    return cfg


@pytest.fixture()
def live_api_client() -> ApiClient:
    cfg = _require_live_config()
    with ApiClient(cfg) as client:
        yield client


@pytest.fixture()
def live_apis(live_api_client):
    return {
        "jobs": JobsApi(live_api_client),
        "output": OutputApi(live_api_client),
        "system": SystemApi(live_api_client),
    }


def _choose_processing_type(system_api: SystemApi):
    available = system_api.get_types().types or []
    if not available:
        pytest.skip("No processing types returned from /types.")

    preferred = next((pt for pt in available if pt.type == "passthru"), None)
    return preferred or available[0]


def _sample_file_for_type(proc_type):
    mime_list = (proc_type.input.mime_in if proc_type.input else None) or []
    pdf_path = Path(__file__).resolve().parent / "test_pdf.pdf"

    for mime in mime_list:
        if mime.startswith("text/"):
            return "sample.txt", b"hello from bsub integration test\n"
        if mime == "application/json":
            return "sample.json", b'{"message": "hello"}'
        if mime == "application/pdf":
            return pdf_path.name, pdf_path.read_bytes()
        if mime == "application/octet-stream":
            return "sample.bin", b"\x00\x01\x02test"

    return "sample.txt", b"hello from bsub integration test\n"


def _wait_for_completion(jobs_api: JobsApi, job_id, timeout_seconds: int = 120):
    deadline = time.time() + timeout_seconds
    last_status = None
    while time.time() < deadline:
        job_resp = jobs_api.get_job(job_id)
        job = getattr(job_resp, "data", job_resp)
        last_status = job.status
        if last_status in {"finished", "failed"}:
            return job
        time.sleep(2)
    pytest.skip(f"Job {job_id} did not finish within {timeout_seconds}s (last status={last_status}); leaving job for inspection.")


def test_live_job_lifecycle(live_apis):
    jobs_api: JobsApi = live_apis["jobs"]
    output_api: OutputApi = live_apis["output"]
    system_api: SystemApi = live_apis["system"]

    proc_type = _choose_processing_type(system_api)
    filename, file_bytes = _sample_file_for_type(proc_type)

    job_id = None
    finished_successfully = False
    try:
        create_resp = jobs_api.create_job(CreateJobRequest(type=proc_type.type))
        job_id = create_resp.data.id
        upload_token = create_resp.data.upload_token

        upload_resp = jobs_api.upload_job_data(job_id, upload_token, (filename, file_bytes))
        assert upload_resp.success is True
        if upload_resp.data_size is not None:
            assert upload_resp.data_size == len(file_bytes)

        submit_resp = jobs_api.submit_job(job_id)
        assert submit_resp.success is True

        job = _wait_for_completion(jobs_api, job_id)
        if job.status == "failed":
            logs = output_api.get_job_logs(job_id)
            pytest.fail(f"Job failed; logs:\n{logs}")

        output = output_api.get_job_output(job_id)
        assert isinstance(output, (bytes, bytearray))
        assert len(output) > 0

        logs = output_api.get_job_logs(job_id)
        assert isinstance(logs, str)
        finished_successfully = True
    finally:
        if job_id is not None and finished_successfully:
            # Clean up only after success; on failure leave the job for inspection.
            try:
                jobs_api.delete_job(job_id)
            except Exception:
                pass


def test_get_job_raises_on_unknown_id(live_apis):
    jobs_api: JobsApi = live_apis["jobs"]
    missing_id = uuid4()

    with pytest.raises(ApiException) as excinfo:
        jobs_api.get_job(missing_id)

    assert excinfo.value.status == 404
