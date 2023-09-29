#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status and displays the response body.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    data = response.json()

    print("Body response:")
    print(f"    - type: {type(data).__name__}")
    print(f"    - content: {data}")
