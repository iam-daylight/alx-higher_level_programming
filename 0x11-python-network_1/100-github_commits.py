#!/usr/bin/python3
"""  fetches gitHub user repo commits  """
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    req = get(url)
    if req.status_code < 400:
        try:
            json_o = req.json()
            for i in range(0, 10):
                print("{}: {}".format(json_o[i].get("sha"),
                                      json_o[i].get('commit').
                                      get('author').get('name')))
        except Exception as er:
            pass
    else:
        print("None")
