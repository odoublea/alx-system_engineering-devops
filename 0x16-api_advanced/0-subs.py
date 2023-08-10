#!/usr/bin/python3
'''
Returns the number of subscribers (not active users, total subscribers) for a
given subreddit
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        Returns 0 if the subreddit is invalid.
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "unxoda"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0  # Subreddit not found


if __name__ == '__main__':
    subreddit = argv[1]
    number_of_subscribers(subreddit)
