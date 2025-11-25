# ListJobs200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[Job]**](Job.md) |  | [optional] 
**total** | **int** | Total number of jobs (before pagination) | [optional] 

## Example

```python
from bsubio.models.list_jobs200_response_data import ListJobs200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobs200ResponseData from a JSON string
list_jobs200_response_data_instance = ListJobs200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ListJobs200ResponseData.to_json())

# convert the object into a dict
list_jobs200_response_data_dict = list_jobs200_response_data_instance.to_dict()
# create an instance of ListJobs200ResponseData from a dict
list_jobs200_response_data_from_dict = ListJobs200ResponseData.from_dict(list_jobs200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


