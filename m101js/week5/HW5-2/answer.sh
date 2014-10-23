#!/usr/bin/env bash

cd small_zips
mongoimport -d test -c zips --drop small_zips.json

cd ../

mongo < ./answer.js

#Get-Content ./answer.js | mongo
