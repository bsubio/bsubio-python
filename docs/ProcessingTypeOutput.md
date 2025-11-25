# ProcessingTypeOutput

Output format information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_out** | **List[str]** | Output MIME types | [optional] 
**ext** | **str** | Output file extension | [optional] 
**display** | **str** | Display format hint | [optional] 

## Example

```python
from bsubio.models.processing_type_output import ProcessingTypeOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingTypeOutput from a JSON string
processing_type_output_instance = ProcessingTypeOutput.from_json(json)
# print the JSON string representation of the object
print(ProcessingTypeOutput.to_json())

# convert the object into a dict
processing_type_output_dict = processing_type_output_instance.to_dict()
# create an instance of ProcessingTypeOutput from a dict
processing_type_output_from_dict = ProcessingTypeOutput.from_dict(processing_type_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


