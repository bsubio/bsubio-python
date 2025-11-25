# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique job identifier | [optional] 
**status** | **str** | Current job status | [optional] 
**type** | **str** | Processing type | [optional] 
**user_id** | **str** | User who created the job | [optional] 
**upload_token** | **str** | Token for uploading data (only present in &#x60;created&#x60; state) | [optional] 
**data_size** | **int** | Size of uploaded data in bytes | [optional] 
**claimed_by** | **str** | Worker ID that claimed the job | [optional] 
**error_code** | **str** | Error code if job failed | [optional] 
**error_message** | **str** | Error message if job failed | [optional] 
**created_at** | **datetime** | Job creation timestamp | [optional] 
**updated_at** | **datetime** | Last update timestamp | [optional] 
**claimed_at** | **datetime** | When job was claimed by worker | [optional] 
**finished_at** | **datetime** | When job finished (success or failure) | [optional] 

## Example

```python
from bsubio.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


