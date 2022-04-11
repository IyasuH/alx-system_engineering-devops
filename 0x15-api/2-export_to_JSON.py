#!/usr/bin/python3
"""
Python script using this REST API for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys
if __name__ == "__main__":
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    x = todo.json()
    perso = requests.get('https://jsonplaceholder.typicode.com/users')
    y = perso.json()
    nam = ""
    temp = {sys.argv[1]: []}
    nm = {}
    nn = []
    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        for b in y:
            if b.get('id') == int(sys.argv[1]):
                nam = b.get("username")
        for a in x:
            if a.get('userId') == int(sys.argv[1]):
                nm = {"task": a.get('title'),
                      "completed": a.get('completed'), "username": nam}
                nn.append(nm)
                temp = {sys.argv[1]: nn}
        f.write(json.dumps(temp))
