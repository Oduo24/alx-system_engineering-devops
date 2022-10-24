#!/usr/bin/python3
"""0-gather_data_from_an_API module"""
import requests
from sys import argv

if __name__ == "__main__":
    try:
        int(argv[1])
    except Exception as e:
        exit(1)

    employeeID = int(argv[1])
    endpoint = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(endpoint, employeeID)).json()
    todo = requests.get(
        "{}/users/{}/todos".format(endpoint, employeeID)).json()
    employeeName = user.get('name')
    completed = 0
    total = 0
    for elem in todo:
        if elem.get('completed') is True:
            total += 1
            completed += 1
        else:
            total += 1

    print("Employee {} is done with tasks({}/{}):".format(employeeName,
                                                          completed,
                                                          total))

    for done in todo:
        if done.get('completed') is True:
            print("\t {}".format(done.get('title')))
