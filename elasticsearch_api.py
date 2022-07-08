#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 15:09:05 2022

@author: liuc36
"""

from elasticsearch import Elasticsearch
import json


def pprint(data):
    """
    Formats output prettily
    :param data: takes in a Python dictionary and prints a nicely formatted JSON object
    """
    json_format=json.dumps(data,indent=4)
    print(json_format)


class ElasticSearchReader:
    """
    Elasticsearch Python connection from https://elasticsearch-py.readthedocs.io/en/v8.3.2/api.html#module-elasticsearch
    :param config: configuration file that contains connection information according to template
    """
    
    def __init__(self, config):
        with open('config.json') as f:
            config_params = json.load(f)
            es_host=config_params['host']
            es_port=config_params['port']
            es_user=config_params['username']
            es_password=config_params['password']
        self.es=Elasticsearch('http://'+es_host+':'+es_port,basic_auth=(es_user, es_password), verify_certs=False)
    

    def search_result(self, index=None, query=None, incl_fields=None, size=None):
        """
        Searches database either in indices. To be used with return_logs and log_count
        :param index: ['index1','index2'...] list of index to search in. None = search in all indices
        :param query: JSON object that defines a query. None = no restrictions. See here for more info: https://www.elastic.co/guide/en/elasticsearch/reference/8.3/query-dsl.html
        :param incl_fields: ['level','pid'...] list of fields to include in return. None = return all fields
        :param size: number of logs to return, default = 10
        :return: object of type ObjectApiResponse, contains results and its query information
        """
        result= self.es.search(index=index,query=query,source_includes=incl_fields,size=size)
        return result
    
    
    def return_logs(self, result):
        """
        Parses the return type of search_result to return log messages that matched query
        :param result: object returned by search_result
        :return: list of Python dictionaries of log messages
        """
        return result['hits']['hits']
    
    
    def log_count(self,result):
        """
        Parses the return type of search_result to return number of log messages that matched query
        :param result: object returned by search_result
        :return: Python dictionary containing field of number of logs that matched query
        """
        return result['hits']['total']


    def list_all_indices(self, verbose=False):
        """
        Returns list of all indices in Elasticsearch instance
        :param verbose: True/False to return additional information about each index
        :return: Python list of all indices
        """
        if verbose:
            return self.es.indices.get(index="*")
        else:
            return list(self.es.indices.get(index="*").keys())
    
