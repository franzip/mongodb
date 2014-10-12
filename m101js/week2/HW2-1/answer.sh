#!/usr/bin/env bash

mongoimport --type csv --headerline weather_data.csv -d weather -c data
npm install mongodb
node ./app.js