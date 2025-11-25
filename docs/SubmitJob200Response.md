# SubmitJob200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from bsubio.models.submit_job200_response import SubmitJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitJob200Response from a JSON string
submit_job200_response_instance = SubmitJob200Response.from_json(json)
# print the JSON string representation of the object
print(SubmitJob200Response.to_json())

# convert the object into a dict
submit_job200_response_dict = submit_job200_response_instance.to_dict()
# create an instance of SubmitJob200Response from a dict
submit_job200_response_from_dict = SubmitJob200Response.from_dict(submit_job200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


