#!/usr/bin/python3
""" This script queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Returns a list containing the titles of all hot articles """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {'User-Agent': 'curious'}

    resp = requests.get(url, params={"after": after}, headers=user_agent)
    if resp.status_code != 200:
        return None
    if after is None:
        return hot_list

    data = resp.json()
    for post in data['data']['children']:
        title = post['data']['title']
        hot_list.append(title)
    after = data['data']['after']

    return recurse(subreddit, hot_list, after)
