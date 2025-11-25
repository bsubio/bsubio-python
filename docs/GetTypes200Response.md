# GetTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[ProcessingType]**](ProcessingType.md) |  | [optional] 

## Example

```python
from bsubio.models.get_types200_response import GetTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTypes200Response from a JSON string
get_types200_response_instance = GetTypes200Response.from_json(json)
# print the JSON string representation of the object
print(GetTypes200Response.to_json())

# convert the object into a dict
get_types200_response_dict = get_types200_response_instance.to_dict()
# create an instance of GetTypes200Response from a dict
get_types200_response_from_dict = GetTypes200Response.from_dict(get_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


