#!/usr/bin/env bash

mongorestore dump
npm install
node app.js