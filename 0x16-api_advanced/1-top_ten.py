#!/usr/bin/python3
"""
Queries Reddit API
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts for given subreddit
    """
    if (type(subreddit) is not str):
        print(None)
    url_api = ("https://reddit.com/r/{}/hot.json".format(subreddit))
    users = requests.get(url_api, headers={'User-Agent': 'chrome'})
    use = users.json()
    if users.status_code != 200:
        print(None)
    else:
        for x in range(10):
            print(use['data']['children'][x]['data']['title'])
