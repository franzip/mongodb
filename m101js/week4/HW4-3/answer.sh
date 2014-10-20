#!/usr/bin/env bash

cd blog
mongo < ./answer.js
# Get-Content ./answer.js | mongo
npm install
cd ../validate
npm install
node hw4-3_validate.js
