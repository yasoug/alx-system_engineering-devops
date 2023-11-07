#!/usr/bin/python3
""" This script queries the Reddit API
and prints keyword with their occurrences """
import requests


def count_words(subreddit, word_list, result=[], after=None):
    """ Returns occurrences of words in a hot articles """
    user_agent = {'User-Agent': 'curious'}
    resp = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                        .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if resp.status_code == 200:
        data = resp.json()
        after = data['data']['after']
        for post in data['data']['children']:
            title = post['data']['title'].split(' ')
            for words in title:
                word = words.lower()
                if word in word_list:
                    result.append(word)
        if after is not None:
            count_words(subreddit, word_list, result, after)
        else:
            dict_res = {}
            for word in word_list:
                dict_res[word] = 0
            for i in result:
                dict_res[i] += 1
            for v in sorted(dict_res.values(), reverse=True):
                for k in dict_res:
                    if dict_res[k] == v and v != 0:
                        print("{}: {}".format(k, v))
    else:
        return
