import requests
import json
from requests_oauthlib import OAuth1
# Get Memberships of a Board
print("-----Get Memberships of a Board-----")
idBoard = "5eb9ba14074fa644a2dac98f"
url = "https://api.trello.com/1/boards/"+idBoard+"/memberships"
auth = OAuth1('b7dc2a47ed291aefddf602a6638a5e0f', '5e6f6cd54fe8121a2dbc9253',
              '2849ddb50c19c14b4af499efe20f350ce4e17e36070fb7f35b49a68069edfcfd', '7cce4e7d5be9d424e7c8efc64572308c5ae15ee840b0a5e75eeb617eb55c2272')
headers = {
    "Accept": "application/json"
}
response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)
print("Status: " + str(response.status_code))
print(json.dumps(json.loads(response.text),
                 sort_keys=True, indent=4, separators=(",", ": ")))

# Get a Board
print("-----Get a Board-----")
idBoard = "5eb9ba14074fa644a2dac98f"
url = "https://api.trello.com/1/boards/"+idBoard
response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
)
print("Status: " + str(response.status_code))
print(json.dumps(json.loads(response.text),
                 sort_keys=True, indent=4, separators=(",", ": ")))
