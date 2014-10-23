#!/usr/bin/env bash

cd grades
mongoimport -d test -c grades --drop grades.json

cd ../

mongo < ./answer.js

# Get-Content ./answer.js | mongo