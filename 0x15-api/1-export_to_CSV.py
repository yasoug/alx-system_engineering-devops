#!/usr/bin/python3
"""
This script uses a given API, for a given employee ID,
and returns information about his/her TODO list progress
then exports data in the CSV format
"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    name = get(url + "/users/{}".format(argv[1])).json().get("username")
    todos = get(url + "/user/{}/todos".format(argv[1])).json()

    with open("{}.csv".format(argv[1]), mode="w") as csvfile:
        file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            file.writerow([argv[1], name, task.get("completed"),
                           task.get("title")])
