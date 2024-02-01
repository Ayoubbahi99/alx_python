#!/usr/bin/python3
"""import libraries"""
import requests
import sys
"""Get the username and password"""
username = sys.argv[1]
password = sys.argv[2]

"""get the authentication of the gathered info"""
response = requests.get("https://api.github.com/user", auth=(username, password))
"""Get ID"""
if response.status_code == 200:
    print(response.json().get("id"))
else:
    print("None")