#!/usr/bin/python3
"""
Python script using this REST API for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import json
import requests
import sys
if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    x = todo.json()
    perso = requests.get('https://jsonplaceholder.typicode.com/users')
    y = perso.json()
    nam = ""
    temp = {}
    nm = {}
    nn = []
    with open('todo_all_employees.json', 'w') as f:
        for b in y:
            nam = b.get("username")
            for a in x:
                nm = {"username": nam, "task": a.get('title'),
                      "completed": a.get('completed')}
                nn.append(nm)
                temp = {str(b.get("id")): nn}
        f.write(json.dumps(temp))
