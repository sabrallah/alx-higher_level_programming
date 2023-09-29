#!/usr/bin/python3
"""
This script fetches and prints the latest 10 commits from a GitHub repository.
Usage: ./100-github_commits.py repository owner
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./100-github_commits.py repository owner")

    repository = sys.argv[1]
    owner = sys.argv[2]

    # Make a GET request to the GitHub API to fetch the commits
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    # Check the rate limit remaining in the response headers
    rate_limit_remaining = int(response.headers['X-RateLimit-Remaining'])

    if rate_limit_remaining == 0:
        sys.exit("API rate limit exceeded. Please try again later.")

    if response.status_code == 200:
        commits = response.json()[:10]  # Get the latest 10 commits
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        sys.exit(f"Error: Unable to fetch commits. Status code:
                 {response.status_code}")
