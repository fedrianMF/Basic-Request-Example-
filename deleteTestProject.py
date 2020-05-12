import requests
from requests.auth import HTTPBasicAuth

url = "https://carlosgutierrezsanjines.atlassian.net/rest/api/2/project/10005"

auth = HTTPBasicAuth("carlos.gutierrez@fundacion-jala.org",
                     "gbOJ8Ney7LLGjW7eBG2a48AB")

response = requests.request(
    "DELETE",
    url,
    auth=auth
)

print(response.status_code)
