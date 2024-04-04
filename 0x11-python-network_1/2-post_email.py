#!/usr/bin/python3
"""  post an email  """
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode()
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
