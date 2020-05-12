"""
Get users accountId.
"""

import json
import requests
from requests.auth import HTTPBasicAuth


URL = 'https://carlosgutierrezsanjines.atlassian.net/rest/api/2/myself'

authorization = HTTPBasicAuth(
    'carlos.gutierrez@fundacion-jala.org', 'gbOJ8Ney7LLGjW7eBG2a48AB')

response = requests.get(URL, auth=authorization)
response.raise_for_status()

data = json.loads(response.text)

""" print(json.dumps(json.loads(response.text),
                 sort_keys=True, indent=4, separators=(",", ": "))) """

print("Expecting OK status: " + str(response.status_code == 200))
print(data['accountId'])
