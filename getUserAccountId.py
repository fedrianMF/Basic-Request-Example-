import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://carlosgutierrezsanjines.atlassian.net/rest/api/2/myself'

authorization = HTTPBasicAuth(
    'carlos.gutierrez@fundacion-jala.org', 'gbOJ8Ney7LLGjW7eBG2a48AB')

response = requests.get(url, auth=authorization)
response.raise_for_status()

data = json.loads(response.text)

""" print(json.dumps(json.loads(response.text),
                 sort_keys=True, indent=4, separators=(",", ": "))) """

print(data['accountId'])
