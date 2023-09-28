#!/bin/bash

STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ $STATUS -eq 200 ]; then
  curl -s "$1"
fi
