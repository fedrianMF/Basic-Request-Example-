import requests
import json
from requests.auth import HTTPBasicAuth

URL = "https://alvaroolivera.atlassian.net/rest/api/2/issue/TP1-1/comment"

AUTH = HTTPBasicAuth("Alvaro.Olivera@fundacion-jala.org", "hU3qBKyOzzRBFurcBLIy5D8A")

HEADERS = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

PAYLOAD = json.dumps( {
    "body": "Hello World from python"
} )

response = requests.request(
    "POST",
    URL,
    data=PAYLOAD,
    headers=HEADERS,
    auth=AUTH
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
