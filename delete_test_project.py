"""
Delete a project by its ID needs modifications.
"""

import requests
from requests.auth import HTTPBasicAuth

URL = "https://carlosgutierrezsanjines.atlassian.net/rest/api/2/project/10006"

auth = HTTPBasicAuth("carlos.gutierrez@fundacion-jala.org",
                     "gbOJ8Ney7LLGjW7eBG2a48AB")

response = requests.request(
    "DELETE",
    URL,
    auth=auth
)

print("Expecting No_Contet status: " + str(response.status_code == 204))
