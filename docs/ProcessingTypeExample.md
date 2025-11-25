# ProcessingTypeExample

Example usage information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmd** | **str** | Example command | [optional] 
**desc** | **str** | Example description | [optional] 

## Example

```python
from bsubio.models.processing_type_example import ProcessingTypeExample

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingTypeExample from a JSON string
processing_type_example_instance = ProcessingTypeExample.from_json(json)
# print the JSON string representation of the object
print(ProcessingTypeExample.to_json())

# convert the object into a dict
processing_type_example_dict = processing_type_example_instance.to_dict()
# create an instance of ProcessingTypeExample from a dict
processing_type_example_from_dict = ProcessingTypeExample.from_dict(processing_type_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


