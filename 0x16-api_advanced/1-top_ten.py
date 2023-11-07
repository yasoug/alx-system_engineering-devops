#!/usr/bin/python3
""" This script queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """ Returns the first 10 hot posts, or None if invalid subreddit """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    user_agent = {'User-Agent': 'curious'}

    resp = requests.get(url, headers=user_agent)
    if resp.status_code == 200:
        data = resp.json()
        for post in data['data']['children']:
            title = post['data']['title']
            print(title)
    else:
        print(None)
