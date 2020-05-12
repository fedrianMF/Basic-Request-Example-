import requests
import json
from requests_oauthlib import OAuth1

url = 'https://api.trello.com/1/boards/{id}/memberships'
auth = OAuth1('b7dc2a47ed291aefddf602a6638a5e0f', '5e6f6cd54fe8121a2dbc9253','7cce4e7d5be9d424e7c8efc64572308c5ae15ee840b0a5e75eeb617eb55c2272', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))