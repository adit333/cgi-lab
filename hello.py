#!/usr/bin/env python3

import os
import json

import templates

# Q1
env = {}

for key, value in os.environ.items():
    env[key] = value

print("Content-Type: application/json")
print()

print(json.dumps(env, indent=4))

#Q2
print()
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
message = "\nQuery string:{}".format(os.environ.get('QUERY_STRING'))
print(message)

#Q3
print("<br>")
message = "\nBrowser:{}".format(os.environ.get("HTTP_USER_AGENT"))
print(message)
print("<br>")
