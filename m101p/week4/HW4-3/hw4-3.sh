#!/usr/bin/env bash

# import data...
mongoimport -d blog -c posts < posts.json

# on Windows run:
# Get-Content posts.json | mongoimport -d blog -c posts < posts.json

# create indexes...
mongo < indexes.json

# on Windows run:
# Get-Content indexes.js | mongo