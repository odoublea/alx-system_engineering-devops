#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/
TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
and non-completed tasks
Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
from sys import argv, exit

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    employee_name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response2 = requests.get(url)
    tasks = response2.json()

    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get('completed')]
    completed = len(completed_tasks)

    text = 'Employee {} is done with tasks({}/{}):'.format(
        employee_name, completed, total_tasks)
    print(text)
    for task in completed_tasks:
        print(f'\t {task.get("title")}')
