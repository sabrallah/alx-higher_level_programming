#!/usr/bin/python3

# This script sends a POST request to a given URL with an email as a parameter
# and displays the body of the response.

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Retrieve the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter as UTF-8
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request with the URL and encoded data
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and retrieve the response
    with urllib.request.urlopen(req) as response:
        # Read the response body and decode it as UTF-8
        body = response.read().decode('utf-8')

        # Print the response body
        print(body)
