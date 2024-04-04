#!/usr/bin/python3
"""  Read the body of a request by handling exceptions  """
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Failed: {}".format(e.reason))
