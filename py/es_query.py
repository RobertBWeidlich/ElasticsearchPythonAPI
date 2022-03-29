#!/usr/bin/env python3
#-*- coding: utf-8 -*-
########################################################################
# file:    es_query.py
# date:    Tue Mar 29 10:27:57 EDT 2022 
# purpose: simple search using the python elasticsearch library
# todo:    implement more complex searches
########################################################################
from elasticsearch import Elasticsearch
import json
import requests
import pprint as pp

#cluster_address = "https://localhost:9200"
cluster_address = "http://localhost:9200"

# create a client instance of Elasticsearch
elastic_client = Elasticsearch(cluster_address)

search_param = {
    'query': {
        'match_all': {}
    }
}

# create a Python dictionary for the search query:
search_param_orig = {
    "query": {
        "terms": {
            "_id": [ 1234, 42 ] # find Ids '1234' and '42'
        }
    }
}

# get a response from the cluster
response = elastic_client.search(index="index-sysmon-20220118-1540", body=search_param)
print ('response:', response)

# todo: this doesn't work; response is type
# <class 'elastic_transport.ObjectApiResponse'>
#pp.pprint(response)


