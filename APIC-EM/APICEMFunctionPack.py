import requests
import json
from tabulate import *


def get_NetworkHostInventory(api_url, ticket):

    api_url = api_url + "/api/v1/host"
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    print("Status of /host request: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception(
            "Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    host_list = []
    i = 0
    for item in response_json["response"]:
        i += 1
        host = [
            i,
            item["hostType"],
            item["hostIp"]
        ]
        host_list.append(host)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))
