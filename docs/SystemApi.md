# bsubio.SystemApi

All URIs are relative to *https://app.bsub.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_types**](SystemApi.md#get_types) | **GET** /v1/types | Get available processing types
[**get_version**](SystemApi.md#get_version) | **GET** /v1/version | Get API version


# **get_types**
> GetTypes200Response get_types()

Get available processing types

Returns a list of all processing types supported by the workers.
Use these types when creating jobs.


### Example


```python
import bsubio
from bsubio.models.get_types200_response import GetTypes200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)


# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.SystemApi(api_client)

    try:
        # Get available processing types
        api_response = api_instance.get_types()
        print("The response of SystemApi->get_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTypes200Response**](GetTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of processing types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> GetVersion200Response get_version()

Get API version

Returns version information for the API server

### Example


```python
import bsubio
from bsubio.models.get_version200_response import GetVersion200Response
from bsubio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.bsub.io
# See configuration.py for a list of all supported configuration parameters.
configuration = bsubio.Configuration(
    host = "https://app.bsub.io"
)


# Enter a context with an instance of the API client
with bsubio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bsubio.SystemApi(api_client)

    try:
        # Get API version
        api_response = api_instance.get_version()
        print("The response of SystemApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVersion200Response**](GetVersion200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

