#!/usr/bin/env bash

mongoimport -d school -c students < students.json

# On Windows:
# Get-Content students.json | mongoimport -d school -c students 