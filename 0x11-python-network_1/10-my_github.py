#!/usr/bin/python3
"""
This script retrieves the GitHub user ID
using the GitHub API and Basic Authentication.
"""

import requests
import sys


def get_github_id(username, personal_access_token):
    """
    Get the GitHub user ID using the GitHub API and Basic Authentication.

    Args:
        username (str): Your GitHub username.
        personal_access_token (str): Your personal access token.

    Returns:
        int: The GitHub user ID if successful, None otherwise.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"token {personal_access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("id")
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    github_id = get_github_id(username, personal_access_token)

    if github_id is not None:
        print(github_id)
    else:
        print("None")
