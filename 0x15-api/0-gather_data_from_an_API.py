#!/usr/bin/python3
"""This module gathers data from an API"""
from os import sys
import requests

employee_id = int(sys.argv[1])
employee_name = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()["name"]
todo_list = requests.get('https://jsonplaceholder.typicode.com/todos').json()

total_tasks = 0
total_tasks_done = 0
titles_of_completed_tasks = []

for todo in todo_list:
    if todo["userId"] == employee_id:
        total_tasks += 1
        if todo["completed"] == True:
            total_tasks_done += 1
            titles_of_completed_tasks.append(todo["title"])



print('Employee {} is done with tasks {}/{}:'.format(employee_name, total_tasks_done, total_tasks))

for title in titles_of_completed_tasks:
    print('\t {}'.format(title))
