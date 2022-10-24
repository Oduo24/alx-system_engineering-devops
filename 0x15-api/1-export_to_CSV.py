#!/usr/bin/python3
"""1-export_to_CSV module"""
import csv
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
    employeeName = user.get('username')

    with open('{}.csv'.format(employeeID), 'w', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for elem in todo:
            row = [employeeID, employeeName, elem.get(
                'completed'), elem.get('title')]
            writer.writerow(row)
