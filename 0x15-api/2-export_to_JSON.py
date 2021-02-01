#!/usr/bin/python3
"""
Return info about an user for a given ID to csv file -- REST API
"""
import json
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(sys.argv[1])).json()
    posts = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    username = user[0].get("username")
    data_list = [{"task": p.get("title"), "completed": p.get("completed"),
                  "username": username} for p in posts]
    data_dict = {sys.argv[1]: data_list}
    with open("{}.json".format(sys.argv[1]), mode="w") as out:
        json.dump(data_dict, out)
