import requests
import json
from requests_oauthlib import OAuth1
# Create a List on a Board
print("-----Create a List on a Board-----")
idBoard = "5eb9ba14074fa644a2dac98f"
nameList = "Test Felix"
url = "https://api.trello.com/1/boards/"+idBoard+"/lists"
auth = OAuth1('b7dc2a47ed291aefddf602a6638a5e0f', '5e6f6cd54fe8121a2dbc9253',
              '2849ddb50c19c14b4af499efe20f350ce4e17e36070fb7f35b49a68069edfcfd', '7cce4e7d5be9d424e7c8efc64572308c5ae15ee840b0a5e75eeb617eb55c2272')
query = {
    'name': nameList
}
headers = {
    "Accept": "application/json"
}
response = requests.request(
    "POST",
    url,
    auth=auth,
    params=query
)
print("Status: " + str(response.status_code))
print(response.text)
#Response: {"id":"5ebac11236a55e4a5bf37cf4","name":"Test Felix","closed":false,"pos":32767.5,"idBoard":"5eb9ba14074fa644a2dac98f","limits":{}}
#test .PY