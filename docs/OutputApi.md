# bsubio.OutputApi

All URIs are relative to *https://app.bsub.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_logs**](OutputApi.md#get_job_logs) | **GET** /v1/jobs/{jobId}/logs | Get job logs (stderr)
[**get_job_output**](OutputApi.md#get_job_output) | **GET** /v1/jobs/{jobId}/output | Get job output (stdout)


# **get_job_logs**
> str get_job_logs(job_id)

Get job logs (stderr)

Returns the standard error (stderr) from the job processing.
Useful for debugging failed jobs.


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
    api_instance = bsubio.OutputApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Get job logs (stderr)
        api_response = api_instance.get_job_logs(job_id)
        print("The response of OutputApi->get_job_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutputApi->get_job_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job logs |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_output**
> bytearray get_job_output(job_id)

Get job output (stdout)

Returns the standard output (stdout) from the job processing.
Only available for finished jobs.


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
    api_instance = bsubio.OutputApi(api_client)
    job_id = 'a1b2c3d4-e5f6-7890-abcd-ef1234567890' # str | Unique job identifier (UUID)

    try:
        # Get job output (stdout)
        api_response = api_instance.get_job_output(job_id)
        print("The response of OutputApi->get_job_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutputApi->get_job_output: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Unique job identifier (UUID) | 

### Return type

**bytearray**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job output |  -  |
**401** | Unauthorized - Invalid or missing API key |  -  |
**404** | Resource not found |  -  |
**409** | Job not finished yet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

