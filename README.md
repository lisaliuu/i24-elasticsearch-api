# i24-elasticsearch-api

Queries from Elasticsearch using [Python Elasticsearch client](https://elasticsearch-py.readthedocs.io/en/v8.3.2/).

## Set up:
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


