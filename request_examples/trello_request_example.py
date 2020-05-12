"""Module for TRELLO request"""
import json
from http import HTTPStatus
import requests
from requests_oauthlib import OAuth1
from assertpy import assert_that

URL = "https://api.trello.com/1/members/me/boards"

AUTH = OAuth1('668fe425619b44578f6b5dd9a02e09a4',
              'c96a92fc1940b3648744f19ab5bca9a3c49213dea7c08f8a5c8bb068b9674183',
              'c96a92fc1940b3648744f19ab5bca9a3c49213dea7c08f8a5c8bb068b9674183',
              '68665b1c48cc20381d1c7f3f75f80db7298cba95a02dbc86a564bf9890aa83e8')

HEADERS = {
    "Accept": "application/json"
}

RESPONSE = requests.request("GET", URL, headers=HEADERS, auth=AUTH)

assert_that(RESPONSE.status_code).is_equal_to(HTTPStatus.OK.value)
print(json.dumps(RESPONSE.json(), sort_keys=True, indent=4, separators=(",", ": ")))
