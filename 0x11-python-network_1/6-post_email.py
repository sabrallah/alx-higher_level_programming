#!/usr/bin/python3
"""
Sends a POST request to a URL with an email
as a parameter and displays the response body.
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

    print("Your email is: {}".format(email))
    print(response.text)
