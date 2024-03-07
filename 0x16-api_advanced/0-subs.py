#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return "nonexisting subreddit"

    if response.status_code != 200:
        return "error"

    data = response.json().get("data")
    if not data:
        return "error"

    subscribers = data.get("subscribers")
    if subscribers is None:
        return "error"

    return "existing subreddit"
