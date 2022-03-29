#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# file:    es_ingest.py
# date:    Tue Mar 29 12:47:02 EDT 2022
# purpose: ingest of file of data in ndjson format to Elasticsearch
#          using the python elasticsearch library
# todo:    Allow user to specify index name from command line
########################################################################
import datetime
import elasticsearch
import elasticsearch.helpers
import ndjson
import os
import sys
import pathlib

from pprint import pprint

# CHANGE THESE PARAMETERS AS NEEDED
username = ""
password = ""
#cluster_address = "https://localhost:9200"
cluster_address = "http://localhost:9200"

def es_ingest(pathname):
    input_file = pathlib.Path(pathname)
    if not input_file.exists():
        print(f'File "{pathname}"does not exist')
        return(False)

    """
    es = elasticsearch.Elasticsearch(hosts=cluster_address,
                                      http_auth=(username, password),
                                      verify_certs=False)
    """
    es = elasticsearch.Elasticsearch(hosts=cluster_address,
                                     bearer_auth=(username, password),
                                     verify_certs=False)

    print(f'ingesting "{pathname}"')
    with open(input_file) as inf:
        json_data = ndjson.load(inf)
        for each_doc in json_data:
            if "_id" in each_doc:
                del each_doc["_id"]
            if "_score" in each_doc:
                del each_doc["_score"]
            each_doc["_index"] = "index-rbw-20220329-12"

        try:
            results = elasticsearch.helpers.bulk(es, json_data)
        except Exception as ex:
            print(f'Error: {ex}')

        if len(results[1]) > 0:
            print('* ERRORS on ingest')
        else:
            print('* No errors')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} ndjson-file")
        sys.exit(1)
    es_ingest(sys.argv[1])
    sys.exit(1)

