# bsubio.JobsApi

All URIs are relative to *https://app.bsub.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **POST** /v1/jobs/{jobId}/cancel | Cancel a job
[**create_job**](JobsApi.md#create_job) | **POST** /v1/jobs | Create a new job
[**delete_job**](JobsApi.md#delete_job) | **DELETE** /v1/jobs/{jobId} | Delete a job
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{jobId} | Get job details
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /v1/jobs | List jobs
[**submit_job**](JobsApi.md#submit_job) | **POST** /v1/jobs/{jobId}/submit | Submit job for processing
[**upload_job_data**](JobsApi.md#upload_job_data) | **POST** /v1/upload/{jobId} | Upload data to a job


# **cancel_job**
> CancelJob200Response cancel_job(job_id)

Cancel a job

Cancels a pending or in-progress job.
Finished or failed jobs cannot be cancelled.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.cancel_job200_response import CancelJob200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Cancel a job
        api_response = api_instance.cancel_job(job_id)
        print("The response of JobsApi->cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

[**CancelJob200Response**](CancelJob200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job cancelled successfully |  -  |
**400** | Job cannot be cancelled |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> CreateJob201Response create_job(create_job_request)

Create a new job

Creates a new job and returns a job ID and upload token.
The upload token is required for uploading data to the job.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.create_job201_response import CreateJob201Response
from bsubio.models.create_job_request import CreateJobRequest
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    create_job_request = bsubio.CreateJobRequest() # CreateJobRequest | 

    try:
        # Create a new job
        api_response = api_instance.create_job(create_job_request)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)|  | 

### Return type

[**CreateJob201Response**](CreateJob201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job created successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job**
> delete_job(job_id)

Delete a job

Deletes a job and its associated data.
Only finished or failed jobs can be deleted.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Delete a job
        api_instance.delete_job(job_id)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Job deleted successfully |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |
**409** | Job cannot be deleted (still in progress) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> CreateJob201Response get_job(job_id)

Get job details

Returns detailed information about a specific job

### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.create_job201_response import CreateJob201Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Get job details
        api_response = api_instance.get_job(job_id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

[**CreateJob201Response**](CreateJob201Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job details |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> ListJobs200Response list_jobs(status=status, limit=limit)

List jobs

Returns a paginated list of jobs for the authenticated user.
Results can be filtered by status and limited.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.list_jobs200_response import ListJobs200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    status = 'finished' # str | Filter by job status (optional)
    limit = 20 # int | Maximum number of jobs to return (optional) (default to 20)

    try:
        # List jobs
        api_response = api_instance.list_jobs(status=status, limit=limit)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by job status | [optional] 
 **limit** | **int**| Maximum number of jobs to return | [optional] [default to 20]

### Return type

[**ListJobs200Response**](ListJobs200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job**
> SubmitJob200Response submit_job(job_id)

Submit job for processing

Submits a job for processing after data has been uploaded.
The job moves from 'loaded' to 'pending' state and enters the queue.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.submit_job200_response import SubmitJob200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Submit job for processing
        api_response = api_instance.submit_job(job_id)
        print("The response of JobsApi->submit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->submit_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

[**SubmitJob200Response**](SubmitJob200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job submitted successfully |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_job_data**
> UploadJobData200Response upload_job_data(job_id, token, file)

Upload data to a job

Uploads the input file for processing. Requires the upload token
obtained when creating the job.


### Example

* Bearer (API Key) Authentication (BearerAuth):

```python
import bsubio
from bsubio.models.upload_job_data200_response import UploadJobData200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): BearerAuth
configuration = bsubio.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.JobsApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    token = 'token_example' # str | Upload token from job creation
    file = None # bytearray | File to process

    try:
        # Upload data to a job
        api_response = api_instance.upload_job_data(job_id, token, file)
        print("The response of JobsApi->upload_job_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->upload_job_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **token** | **str**| Upload token from job creation | 
 **file** | **bytearray**| File to process | 

### Return type

[**UploadJobData200Response**](UploadJobData200Response.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded successfully |  -  |
**400** | Invalid request |  -  |
**401** | Invalid upload token |  -  |
**404** | Resource not found |  -  |
**413** | File too large |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

