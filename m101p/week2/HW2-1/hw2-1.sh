#!/usr/bin/env bash

mongoimport -d students -c grades < grades.js

# On Windows:
# Get-Content grades.js | mongoimport -d students -c grades