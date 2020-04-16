import json
import requests

def get_ticket():
    requests.packages.urllib3.disable_warnings()

    api_url = "https://{YOUR-APICEM}.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "!!!REPLACE ME with the Username!!!",
        "password": "!!!REPLACE ME with the Password!!!"
    }

    resp = requests.post(api_url, json.dumps(body_json),
                         headers=headers, verify=False)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    print("The service ticket number is: ", serviceTicket)

    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    print("The service ticket number is: ", serviceTicket)

    return serviceTicket
