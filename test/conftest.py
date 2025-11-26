import pytest

# These modules are generated placeholders for integration tests against the
# live BSUB.IO API. Mark them as skipped so the test suite doesn't report
# misleading greens until real coverage is added.
PLACEHOLDER_MODULES = {
    "test_cancel_job200_response",
    "test_create_job201_response",
    "test_error",
    "test_get_types200_response",
    "test_get_version200_response",
    "test_job",
    "test_jobs_api",
    "test_list_jobs200_response",
    "test_list_jobs200_response_data",
    "test_output_api",
    "test_processing_type",
    "test_processing_type_example",
    "test_processing_type_input",
    "test_processing_type_output",
    "test_submit_job200_response",
    "test_system_api",
    "test_upload_job_data200_response",
}


def pytest_collection_modifyitems(config, items):
    skip_placeholder = pytest.mark.skip(reason="Generated placeholder; requires live API coverage.")
    for item in items:
        module_name = item.module.__name__.rsplit(".", 1)[-1]
        if module_name in PLACEHOLDER_MODULES:
            item.add_marker(skip_placeholder)
