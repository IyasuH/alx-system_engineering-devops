#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """
    if (type(subreddit) is not str):
        return(0)
    url_api = ("https://reddit.com/r/{}/about.json".format(subreddit))
    users = requests.get(url_api, headers={'User-Agent': 'chrome'})
    use = users.json()
    if users.status_code != 200:
        return(0)
    return(users.json().get("data").get("subscribers"))
