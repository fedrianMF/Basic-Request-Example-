import requests
import json
from requests.auth import HTTPBasicAuth

expected_result = [[200, "AT Bootcamp"], [200, "Test Project 1"]]

URL_List = ["https://alvaroolivera.atlassian.net/rest/api/2/project/AB",
      "https://alvaroolivera.atlassian.net/rest/api/2/project/TP1"]

AUTH = HTTPBasicAuth("Alvaro.Olivera@fundacion-jala.org", "hU3qBKyOzzRBFurcBLIy5D8A")

HEADERS = {
   "Accept": "application/json"
}

index = 0
for URL in URL_List:
   response = requests.request(
      "GET",
      URL,
      headers=HEADERS,
      auth=AUTH
   )
   print(response.status_code)
   print("Ok" if response.status_code == expected_result[index][0] else "Failed")
   print(response.json()["name"])
   print("Ok" if response.json()["name"] == expected_result[index][1] else "Failed")
   index += 1
   print("")
   #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
