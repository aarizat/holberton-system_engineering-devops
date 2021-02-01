#!/usr/bin/python3
"""
Return info of all users to json file -- REST API
"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    posts = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    data = {}
    for user in users:
        data[user.get("id")] = [{"username": user.get("username"),
                                 "task": p.get("title"),
                                 "completed": p.get("completed")}
                                for p in posts
                                if user.get("id") == p.get("userId")]
    with open("todo_all_employees.json", mode="w") as out:
        json.dump(data, out)
