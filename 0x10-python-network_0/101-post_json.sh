#!/bin/bash
# Script sends JSON POST request to specified URL and displays body of response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
