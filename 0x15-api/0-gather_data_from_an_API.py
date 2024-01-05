#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

user = argv[1]

response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user}')
name = response.json().get('name')
response2 = requests.get(f'https://jsonplaceholder.typicode.com/users/{user}/todos')
completed = 0
task_title = []
for _ in response2.json():
    if _.get('completed') is True:
        task_title.append(_.get('title'))
        completed += 1
print(f'Employee {name} is done with tasks({completed}/{len(response2.json())}):')
for _ in task_title:
    print('\t {}'.format(_))
