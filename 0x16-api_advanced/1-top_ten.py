#!/usr/bin/python3
"""
reddit_utils Module

This module provides functions to interact with the Reddit API and retrieve
information about subreddits and posts.

Functions:
    top_ten(subreddit): Retrieve information about the top 10 hot posts in a
    given subreddit.

Module Usage Example:
    from reddit_utils import top_ten

    subreddit_name = "programming"
    result = top_ten(subreddit_name)
    if result != 0:
        print("Top 10 Hot Posts in r/programming:")
        for post in result["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("Subreddit not found or an error occurred.")
"""

import requests
from sys import argv
import json


def top_ten(subreddit):
    """
    Retrieve information about the top 10 hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve data from.

    Returns:
        dict or int: A dictionary containing information about the top 10 hot
        posts, or 0 if the subreddit is not found or an error occurs.

    Example:
        subreddit_name = "programming"
        result = top_ten(subreddit_name)
        if result != 0:
            print("Top 10 Hot Posts in r/programming:")
            for post in result["data"]["children"]:
                print(post["data"]["title"])
        else:
            return 0
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format({}, subreddit)
    headers = {"User-Agent": "unxoda"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)

        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)

        return title
    else:
        return 0  # Subreddit not found


if __name__ == '__main__':
    subreddit = argv[1]
    top_ten(subreddit)
