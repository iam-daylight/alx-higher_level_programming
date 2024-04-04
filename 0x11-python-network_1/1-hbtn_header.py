#!/usr/bin/python3
"""  Display a value from the header variable  """
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        header = response.info()
        print(header['X-Request-Id'])
