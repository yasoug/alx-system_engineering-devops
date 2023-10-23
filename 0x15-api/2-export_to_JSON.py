#!/usr/bin/python3
"""
This script uses a given API, for a given employee ID,
and returns information about his/her TODO list progress
then exports data in the JSON format
"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = get(url + "/users/{}".format(argv[1])).json().get("username")
    todos = get(url + "/user/{}/todos".format(argv[1])).json()

    task_list = []
    for task in todos:
        task_list.append({"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": name})
    data = {}
    data[argv[1]] = task_list

    with open("{}.json".format(argv[1]), mode="w") as jsonfile:
        json.dump(data, jsonfile)
