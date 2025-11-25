# UploadJobData200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data_size** | **int** | Size of uploaded file in bytes | [optional] 

## Example

```python
from bsubio.models.upload_job_data200_response import UploadJobData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadJobData200Response from a JSON string
upload_job_data200_response_instance = UploadJobData200Response.from_json(json)
# print the JSON string representation of the object
print(UploadJobData200Response.to_json())

# convert the object into a dict
upload_job_data200_response_dict = upload_job_data200_response_instance.to_dict()
# create an instance of UploadJobData200Response from a dict
upload_job_data200_response_from_dict = UploadJobData200Response.from_dict(upload_job_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


