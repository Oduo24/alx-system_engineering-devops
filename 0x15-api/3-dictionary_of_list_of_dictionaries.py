#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module"""
from json import dumps
import requests

if __name__ == "__main__":
    endpoint = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(endpoint)).json()
    users_count = len(users)
    employeeDict = {}

    for user in users:
        employeeName = user.get('username')
        todo = requests.get(
            "{}/users/{}/todos".format(endpoint, user.get('id'))).json()
        row = []
        for elem in todo:
            if elem.get('userId') == user.get('id'):
                dict = {
                    "username": employeeName,
                    "task": elem.get('title'),
                    "completed": elem.get('completed')
                }
                row.append(dict)
            employeeDict[user.get('id')] = row

    with open('todo_all_employees.json', 'w', encoding="utf-8") as file:
        file.write(dumps(employeeDict))
