#!/usr/bin/python3
"""
This script fetches and prints the latest 10 commits from a GitHub repository.
Usage: ./100-github_commits.py repository owner
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    try:
        responses = requests.get(url)
        res_dicts = responses.json()
        for i in range(0, 10):
            print("{}: {}".format(res_dicts[i].get('sha'), res_dicts[i].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
