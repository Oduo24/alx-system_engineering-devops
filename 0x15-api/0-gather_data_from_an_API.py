#!/usr/bin/python3
"""This module gathers data from an API"""
import requests
from os import sys

if __name__ == '__main__':

    employee_id = int(sys.argv[1])
    employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json().get("name")
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    total_tasks = 0
    total_tasks_done = 0
    titles_of_completed_tasks = []

    for todo in todo_list:
        if todo.get("userId") == employee_id:
            total_tasks += 1
            if todo.get("completed") == True:
                total_tasks_done += 1
                titles_of_completed_tasks.append(todo.get("title"))
    print('Employee {} is done with tasks ({}/{}):'.format(employee_name, total_tasks_done, total_tasks))
    for title in titles_of_completed_tasks:
    print('\t {}'.format(title))
