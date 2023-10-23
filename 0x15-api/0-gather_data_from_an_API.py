#!/usr/bin/python3
"""
This script uses a given API, for a given employee ID,
and returns information about his/her TODO list progress
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = get(url + "/users/{}".format(argv[1])).json().get("name")
    todos = get(url + "/user/{}/todos".format(argv[1])).json()

    completed_tasks = []
    for task in todos:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed_tasks), len(todos)))

    for task in completed_tasks:
        print("\t {}".format(task))
