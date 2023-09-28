#!/bin/bash
#This script sends a GET request to a URL and displays the body of the response
curl -sL -X GET "$1" -w "\n%{http_code}" | sed -n '/200/{n;p;q}'
