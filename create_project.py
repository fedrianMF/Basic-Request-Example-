"""
Creates an Example projects, needs modifications.
"""

import json
import requests
from requests.auth import HTTPBasicAuth


URL = "https://carlosgutierrezsanjines.atlassian.net/rest/api/2/project"

auth = HTTPBasicAuth("carlos.gutierrez@fundacion-jala.org",
                     "gbOJ8Ney7LLGjW7eBG2a48AB")

TEMPLATE = "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps({
    "description": "Example Project description",
    "leadAccountId": "70121:8e88568a-6221-49e5-9184-0e48ec8f898b",
    "url": "",
    "projectTemplateKey": TEMPLATE,
    "name": "Example",
    "assigneeType": "PROJECT_LEAD",
    "projectTypeKey": "software",
    "key": "EX"
})

response = requests.request(
    "POST",
    URL,
    data=payload,
    headers=headers,
    auth=auth
)

print("Expecting OK status: " + str(response.status_code == 200))

print(json.dumps(json.loads(response.text),
                 sort_keys=True, indent=4, separators=(",", ": ")))
