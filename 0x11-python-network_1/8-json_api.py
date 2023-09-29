#!/usr/bin/python3
"""
This script takes a letter as an argument and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={"q": q})
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get("id"),
                  json_response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
