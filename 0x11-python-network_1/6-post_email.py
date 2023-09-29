#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email as a parameter.
It then displays the body of the response.

Usage:
    ./6-post_email.py <URL> <email>
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print("Your email is:", email)
    print(response.text)
