#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import sys
import requests
if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
