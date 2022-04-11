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
    with open('{}.csv'.format(sys.argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for b in y:
            if b.get('id') == int(sys.argv[1]):
                nam = b.get("username")
        for a in x:
            if a.get('userId') == int(sys.argv[1]):
                row = [a.get('userId'), nam,
                       a.get('completed'), a.get('title')]
                writer.writerow(row)
