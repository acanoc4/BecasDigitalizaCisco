import requests
import json

requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.1.55/restconf/data/left-interfaces:interfaces"

headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

basicAuth = {
    "username": "cisco",
    "password": "cisco123!"
}

resp = requests.get(api_url, auth=("cisco", "cisco123!"),
                    headers=headers, verify=False)

resp_json = resp.json()

print(resp_json)
