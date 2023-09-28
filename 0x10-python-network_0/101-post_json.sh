#!/bin/bash
# This script sends a JSON POST request to a specified URL and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
