# ProcessingType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type identifier used when creating jobs | [optional] 
**name** | **str** | Human-readable name | [optional] 
**description** | **str** | Human-readable description | [optional] 
**input** | [**ProcessingTypeInput**](ProcessingTypeInput.md) |  | [optional] 
**output** | [**ProcessingTypeOutput**](ProcessingTypeOutput.md) |  | [optional] 
**example** | [**ProcessingTypeExample**](ProcessingTypeExample.md) |  | [optional] 

## Example

```python
from bsubio.models.processing_type import ProcessingType

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingType from a JSON string
processing_type_instance = ProcessingType.from_json(json)
# print the JSON string representation of the object
print(ProcessingType.to_json())

# convert the object into a dict
processing_type_dict = processing_type_instance.to_dict()
# create an instance of ProcessingType from a dict
processing_type_from_dict = ProcessingType.from_dict(processing_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


