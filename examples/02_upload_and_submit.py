import os
import time
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
        # Step 1: Create a job
        job_request = bsubio.CreateJobRequest(type='passthru')
        result = api.create_job(job_request)
        job_id = result.data.id
        upload_token = result.data.upload_token

        print(f'Job created: {job_id}')

        # Step 2: Upload file
        with open('sample.txt', 'rb') as file:  # Replace with your file
            api.upload_job_data(job_id, file, token=upload_token)
        print('File uploaded successfully')

        # Step 3: Submit job for processing
        api.submit_job(job_id)
        print('Job submitted for processing')

        # Step 4: Poll for completion
        status = 'pending'
        while status not in ['finished', 'failed']:
            time.sleep(2)
            result = api.get_job(job_id)
            status = result.data.status
            print(f'Current status: {status}')

        print(f'Job completed with status: {status}')
    except ApiException as e:
        print(f'Error: {e}')
