# i24-elasticsearch-api

Queries from Elasticsearch using [Python Elasticsearch client](https://elasticsearch-py.readthedocs.io/en/v8.3.2/).

## Set up:
Install elasticsearch with `python -m pip install elasticsearch`
Connect to an Elasticsearch instance using a config file according to the template given.

## Features:
- Returns log files that match some query
- Returns the number of log files that match some query
- Lists all the indices in the Elasticsearch instance

## Query Parameter Syntax:
Syntax follows [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/8.3/query-dsl.html).

#### Match one field:
query=
```json
{
    "match": {
        "level": "INFO"
    }
}
```


#### Match multiple fields:
mquery = 
```json
{
   "bool": {
      "must": [
      {
         "match": {
            "level": "INFO"
         }
      },
      {
         "match": {
            "_id": "qDv8ioABjqqRODayRSi1"
         }
      }
      ]
   }
}
```
## Example Use:
```
from elasticsearch_api import ElasticsearchReader

# connect to Elasticsearch
es=ElasticSearchReader("config.json")

#queries in the '.ds-logs-generic-default-2022.05.03-000001' index with 'mquery', outputting the 'level' and 'pid' fields
result=es.search_result(index=['.ds-logs-generic-default-2022.05.03-000001'],query=mquery,incl_fields=['level','pid'])

#return_logs parses result to return the logs as a dictionary
output = es.return_logs(result)

#formats and prints the logs
pprint(output)
```

