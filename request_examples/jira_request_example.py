"""Module for JIRA request"""
import json
from http import HTTPStatus
import requests
from requests.auth import HTTPBasicAuth
from assertpy import assert_that

URL = "https://bc02.atlassian.net/rest/api/2/project"

AUTH = HTTPBasicAuth("joselito28.92@gmail.com", "J38SMFZilX6jXD7e3iFUCA37")

HEADERS = {
    "Accept": "application/json"
}

RESPONSE = requests.request("GET", URL, headers=HEADERS, auth=AUTH)
assert_that(RESPONSE.status_code).is_equal_to(HTTPStatus.OK.value)
print(json.dumps(RESPONSE.json(), sort_keys=True, indent=4, separators=(",", ": ")))
