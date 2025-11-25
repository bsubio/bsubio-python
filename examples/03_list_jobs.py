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
        # List all jobs
        print('Fetching all jobs:')
        result = api.list_jobs()
        print(f'Total jobs: {result.data.total}')
        print(f'Jobs: {len(result.data.jobs)}')

        # List finished jobs only
        print('\nFetching finished jobs:')
        result = api.list_jobs(status='finished', limit=10)

        for job in result.data.jobs:
            print(f'- {job.id}: {job.type} ({job.status})')
    except ApiException as e:
        print(f'Error listing jobs: {e}')
