#!/usr/bin/env bash

mongorestore dump

mongo < answer.js

# Get-Content ./answer.js | mongo