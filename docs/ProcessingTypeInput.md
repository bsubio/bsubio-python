# ProcessingTypeInput

Input format information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_in** | **List[str]** | Accepted input MIME types | [optional] 

## Example

```python
from bsubio.models.processing_type_input import ProcessingTypeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingTypeInput from a JSON string
processing_type_input_instance = ProcessingTypeInput.from_json(json)
# print the JSON string representation of the object
print(ProcessingTypeInput.to_json())

# convert the object into a dict
processing_type_input_dict = processing_type_input_instance.to_dict()
# create an instance of ProcessingTypeInput from a dict
processing_type_input_from_dict = ProcessingTypeInput.from_dict(processing_type_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


