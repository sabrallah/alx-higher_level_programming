#!/bin/bash
# This script checks the HTTP status code of a given URL
URL="https://example.com"  # Replace with the desired URL
# Send a HEAD request to the URL and retrieve the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" $URL)
# Check the status code and display the result
if [ $status_code -eq 100 ]; then
    echo "Status code 100: Continue"
else
    echo "Status code is not 100"
fi
