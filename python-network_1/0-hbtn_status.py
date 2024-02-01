#!/usr/bin/python3

"""Import requests library"""
import requests

"""Get or fetch the website (https://alu-intranet.hbtn.io/status)"""
r = requests.get("https://alu-intranet.hbtn.io/status")
"""Print The requested information by task 0"""
print("Body response:")
print(f"\t- type: {type(r.text)}")
print(f"\t- content: {r.text}")