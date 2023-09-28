#!/bin/bash
# This script sends a request to URL and displays only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
