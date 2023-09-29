#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and display value of X-Request-Id variable found in header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
