#!/usr/bin/python3

"""import sys and requests"""
import sys
import requests

"""
Write a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""
email = sys.argv[2]
data = {'email': email}
r = requests.post(sys.argv[1], data=data)
print(r.text)