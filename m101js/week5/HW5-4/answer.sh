#!/usr/bin/env bash

mongoimport -d test -c zips --drop zips.json

mongo < ./answer.js

# Get-Content ./answer.js | mongo