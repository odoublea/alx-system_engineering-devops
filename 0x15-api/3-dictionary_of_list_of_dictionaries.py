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

import json
import requests
# from sys import argv, exit

if __name__ == '__main__':

    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    employees = response.json()

    employee_tasks = {}

    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('name')

        url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        response2 = requests.get(url)
        tasks = response2.json()

        todo_list = []
        for task in tasks:
            todo_list.append({'username': employee.get('username'),
                              'task': task.get('title'),
                              'completed': task.get('completed')}
                             )

        employee_tasks[employee_id] = todo_list

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(employee_tasks, jsonfile, indent=2)
