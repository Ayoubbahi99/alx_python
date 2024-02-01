#!/usr/bin/python3
"""import requests and sys"""
import requests
import sys

"""get the letter with the help of sys"""
if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

payload = {"q": letter}
response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
"""Use try and exception to check json"""    
try:
    json_response = response.json()
    if json_response:
        print("[{}] {}".format(json_response.get("id"), json_response.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")