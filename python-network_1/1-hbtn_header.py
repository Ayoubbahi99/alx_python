#!/usr/bin/python3

"""Import sys and requests"""
import sys
import requests

"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))

