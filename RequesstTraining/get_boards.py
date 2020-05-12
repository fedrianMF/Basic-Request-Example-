"""
Get project names.
"""

import requests
import json
from requests_oauthlib import OAuth1

url = "https://api.trello.com/1/members/me/boards"

auth = OAuth1('b874df46c1932f121f176125ecc3c52a',
              '01707264bda9655469300c5e744d5b7b1f0bb4aec548191bb8d524190ee380ad',
              '01707264bda9655469300c5e744d5b7b1f0bb4aec548191bb8d524190ee380ad',
              'a1104796d5352c73d54794a0eb3bd3daa1a95fb769b253b19b0c1833cfb33679')

response = requests.get(url, auth=auth)

response.raise_for_status()

boards = json.loads(response.text)

print(json.dumps(json.loads(response.text), sort_keys=True,
      indent=4, separators=(",", ": ")))

names = ['QA board', 'Test Api Trello']

for i in range (len(boards)):
    print(boards[i]['name'] == names[i])