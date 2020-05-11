import requests
import json
from requests.auth import HTTPBasicAuth

URL = "https://bc02.atlassian.net/rest/api/2/project"

AUTH = HTTPBasicAuth("joselito28.92@gmail.com", "J38SMFZilX6jXD7e3iFUCA37")

HEADERS = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   URL,
   headers=HEADERS,
   auth=AUTH
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
