import os
import bsubio
from bsubio.rest import ApiException

# Configure API client
configuration = bsubio.Configuration(
    host="https://app.bsub.io"
)
configuration.access_token = os.environ.get('BSUBIO_API_KEY', 'your-api-key-here')

# Create an instance of the API class
with bsubio.ApiClient(configuration) as api_client:
    api = bsubio.JobsApi(api_client)

    try:
        # Create a new job
        job_request = bsubio.CreateJobRequest(type='passthru')
        result = api.create_job(job_request)

        print('Job created successfully:')
        print(f'Job ID: {result.data.id}')
        print(f'Upload Token: {result.data.upload_token}')
        print(f'Status: {result.data.status}')
    except ApiException as e:
        print(f'Error creating job: {e}')
