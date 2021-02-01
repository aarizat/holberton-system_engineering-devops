#!/usr/bin/python3
"""
Return info about an user for a given ID -- REST API
"""
import requests
import sys


if __name__ == "__main__":
    user = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(sys.argv[1])).json()
    posts = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1])).json()
    username = user[0].get("name")
    titles = [post.get("title") for post in posts if post.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(username,
                                                          len(titles),
                                                          len(posts)))
    print("\t", end='')
    print("\n\t".join(titles))
