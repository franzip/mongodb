#!/usr/bin/env bash

mongorestore dump
npm install mongodb
node app.js