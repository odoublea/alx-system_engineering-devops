#!/usr/bin/python3
'''
Returns the number of subscribers (not active users, total subscribers) for a
given subreddit
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Get the number of subscribers
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "'my-app/0.0.1'"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 404:
        return 0  # Subreddit not found
    else:
        # Handle other error cases here
        return 0


if __name__ == '__main__':
    subreddit = argv[1]
    subscribers_count = number_of_subscribers(subreddit)
    print(f"The subreddit '{subreddit}' has {subscribers_count} subscribers.")