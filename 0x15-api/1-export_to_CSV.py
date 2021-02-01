#!/usr/bin/python3
"""
Return info about an user for a given ID to csv file -- REST API
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(sys.argv[1])).json()
    posts = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    username = user[0].get("username")
    data = [(p.get("userId"), username, p.get("completed"), p.get("title"))
            for p in posts]
    with open("{}.csv".format(sys.argv[1]), mode="w") as out:
        write = csv.writer(out, quoting=csv.QUOTE_ALL)
        write.writerows(data)
