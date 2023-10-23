#!/usr/bin/python3
"""
This script uses a given API, records all tasks from all employees
then exports data in the JSON format
"""
import json
from requests import get


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    names = get(url + "/users/").json()
    data = {}
    task_list = []
    with open("todo_all_employees.json", mode="w") as jsonfile:
        for user in names:
            user_id = user.get('id')
            tasks = get(url + "/user/{}/todos".format(user_id)).json()
            for task in tasks:
                task_list.append({"username": user.get("username"),
                                  "task": task.get("title"),
                                  "completed": task.get("completed")})
                data[user_id] = task_list
            task_list = []
        json.dump(data, jsonfile)
