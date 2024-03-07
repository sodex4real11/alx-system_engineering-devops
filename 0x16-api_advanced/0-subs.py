#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests
def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("Error: Unable to fetch data from Reddit API")
        return None

    data = response.json().get("data")
    if not data:
        print("No data found for the subreddit: {}".format(subreddit))
        return None

    subscribers = data.get("subscribers")
    if subscribers is None:
        print("No subscriber information found for the subreddit: {}".format(subreddit))
        return None

    return subscribers
