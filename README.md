# I24 Elasticsearch API

## Wrapper around Elasticsearch queries with [Python Elasticsearch Client](https://elasticsearch-py.readthedocs.io/en/v8.3.2/).
This Python module is developed for the [I24-MOTION testbed](https://i24motion.org/) data processing pipeline. 

### Motivation
To design functions that wraps around the Elasticsearch client for metrics and logs specific to the lab's needs.

### Result
#### Supported Functions:
- Returns log files that match some query
- Returns the number of log files that match some query
- Lists all the indices in the Elasticsearch instance

#### Example Use:
```python
from elasticsearch_api import ElasticsearchReader
from elasticsearch_api import pprint

# connect to Elasticsearch
es=ElasticsearchReader("config.json")

#queries in the '.ds-logs-generic-default-2022.05.03-000001' index with 'mquery', outputting the 'level' and 'pid' fields
result=es.search_result(index=['.ds-logs-generic-default-2022.05.03-000001'],query=mquery,incl_fields=['level','pid'])

#return_logs parses result to return the logs as a dictionary
output = es.return_logs(result)

#formats and prints the logs
pprint(output)
```
### Set up
1. Install elasticsearch with `python -m pip install elasticsearch`
2. Connect to an Elasticsearch instance using a config file according to the template given.
