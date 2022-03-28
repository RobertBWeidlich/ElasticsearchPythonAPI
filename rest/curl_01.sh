#!/bin/sh
export HOST='localhost'
export PORT='9200'

# 1. Empty query
curl $HOST:$PORT/

# 2. Basic query - shows ???
curl $HOST:$PORT/_search?pretty

# 3. Show indices 
curl $HOST:$PORT/_aliases?pretty

# 4. Show indices in human readable (non-JSON) format
curl $HOST:$PORT/_cat/indices


