"""
Get project member names.
"""

import requests
import json
from requests_oauthlib import OAuth1

url = "https://api.trello.com/1/boards/4LmtdO4W/members"

auth = OAuth1('b874df46c1932f121f176125ecc3c52a',
              '01707264bda9655469300c5e744d5b7b1f0bb4aec548191bb8d524190ee380ad',
              '01707264bda9655469300c5e744d5b7b1f0bb4aec548191bb8d524190ee380ad',
              'a1104796d5352c73d54794a0eb3bd3daa1a95fb769b253b19b0c1833cfb33679')

response = requests.get(url, auth=auth)

response.raise_for_status()

items = json.loads(response.text)

print(json.dumps(json.loads(response.text), sort_keys=True,
      indent=4, separators=(",", ": ")))

members = [
    {
        "id": "5e94747207e81558f342d4be",
        "username": "enriquerivera36",
        "fullName": "Enrique Rivera"
    },
    {
        "id": "5e6f6cd54fe8121a2dbc9253",
        "username": "felixmamani2",
        "fullName": "Felix Mamani"
    }
]

for i in range (len(items)):
    print(items[i] == members[i])