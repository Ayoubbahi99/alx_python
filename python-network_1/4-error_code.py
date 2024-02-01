#!/usr/bin/python3
"""Import sys and requests"""
import sys
import requests

"""
Write a Python script that takes in a URL, 
sends a request to the URL and displays the body of the response.
"""
r = requests.get(sys.argv[1])
code = r.status_code
if code > 400:
    print(f"Error code: {code}")
else:
    print("index")
