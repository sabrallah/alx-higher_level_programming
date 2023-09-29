#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request
to the URL using the requests library,

and displays the value of the
'X-Request-Id' header in the response if it exists.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            # Print the value of 'X-Request-Id' header
            print(response.headers['X-Request-Id'])
    else:
        # If the request was not successful, print an error message
        print("Error: Request failed with status code", response.status_code)
