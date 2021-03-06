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
    tot = 0
    com = 0
    nam = ""
    comm = []
    for a in x:
        if a.get('userId') == int(sys.argv[1]):
            for b in y:
                if b.get('id') == int(sys.argv[1]):
                    nam = b.get('name')
            if a['completed']:
                com = com + 1
                comm.append(a.get('title'))
            else:
                pass
            tot = tot + 1
    print("Employee {} is done with tasks({}/{}):".format(nam, com, tot))
    for b in comm:
        print("\t {}".format(b))
