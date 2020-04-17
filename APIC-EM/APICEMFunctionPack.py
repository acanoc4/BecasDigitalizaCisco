import requests
import json
from tabulate import *
import urllib3

version = "v1"


def get_NetworkHostInventory(api_url, ticket):

    api_url = api_url + "/api/"+version+"/host"
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


def get_IPGeolocation(api_url, ticket, ip):
    api_url = api_url + "/api/"+version+"/ipgeo/"+ip
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

    try:
        for key, value in response_json["response"][ip].items():
            if(value == None):
                print(key + "-->DESCONOCIDO")
            else:
                print(key+"-->"+value)
    except Exception as e:
        print(e)


def get_FlowAnalysis(api_url, ticket):

    api_url = api_url + "/api/"+version+"/flow-analysis"

    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)

    if resp.status_code != 200:
        raise Exception(
            "Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    lista = []

    table_header = ["Numero", "IP Origen", "Puerto Origen",
                    "IP Destino", "Puerto Destino", "Protocolo", "Status"]

    i = 1
    for item in response_json["response"]:
        i += 1
        lista.append([
            i,
            item["sourceIP"],
            item["sourcePort"] if "sourcePort" in lista else "---",
            item["destIP"],
            item["destPort"] if "destPort" in lista else "---",
            item["protocol"] if "protocol" in lista else "---",
            item["status"]
        ])

    print(tabulate(lista, table_header))


def get_Interfaces(api_url, ticket):

    api_url = api_url + "/api/"+version+"/interface"

    headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    resp = requests.get(api_url, headers=headers, verify=False)
    if resp.status_code != 200:
        raise Exception(
            "Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    i = 0
    for item in response_json["response"]:
        i += 1
        print("\n\n=========Interface " + str(i) + " =======")

        for key, value in item.items():
            if(value != "null" and value != "" and value != None):
                print(key + "-->" + value)
