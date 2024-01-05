#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv, exit

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    employee_name = response.json().get('name')

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response2 = requests.get(url)
    tasks = response2.json()

    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get('completed')]
    completed = len(completed_tasks)

    print(f'Employee {employee_name} is done with tasks('
          f'{completed} / {total_tasks}): ')
    for task in completed_tasks:
        print(f'\t {task.get("title")}')
