#!/usr/bin/python3
""" This script queries the Reddit API
and returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers, or 0 if if invalid subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-Agent': 'curious'}

    resp = requests.get(url, headers=user_agent)
    if resp.status_code == 200:
        data = resp.json()
        subscribers = data['data']['subscribers']
        return subscribers
    return 0
