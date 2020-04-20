import json
import requests
from tabulate import tabulate
import xmltodict
from ncclient import manager
import xml.dom.minidom
import json
from tabulate import *
import requests


class YangFunctionPackage:

    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    def __init__(self, ip, username, password):
        self.ip = ip
        self.basicAuth = {
            "username": username,
            "password": password
        }

    def setPassword(self, password):
        self.basicAuth["password"] = password

    def setUsername(self, username):
        self.basicAuth["username"] = username

    def isValid(self):

        requests.packages.urllib3.disable_warnings()

        api_url = "https://"+self.ip+"/restconf/data/ietf-interfaces:interfaces-state/"

        try:
            resp = requests.get(api_url, auth=(
                self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)

            if(resp.status_code >= 200 and resp.status_code <= 299):
                return True
            else:
                return False
        except:
            print("no ha sido posible conectarse al router!")
            return False

    def getIP(self, value):

        requests.packages.urllib3.disable_warnings()

        api_url = "https://"+self.ip + \
            "/restconf/data/ietf-interfaces:interfaces/interface=" + value

        resp = requests.get(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)

        resp_json = resp.json()

        if (resp_json["ietf-interfaces:interface"]["ietf-ip:ipv4"]):
            ip = resp_json["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"]
            return ip
        else:
            return [{"ip": "¯\\_(ツ)_/¯", "netmask": "¯\\_(ツ)_/¯"}]

    def get_dataRestconf(self):

        requests.packages.urllib3.disable_warnings()

        api_url = "https://"+self.ip+"/restconf/data/ietf-interfaces:interfaces-state/"

        resp = requests.get(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)

        resp_json = resp.json()

        cabecera = ["Número", "Nombre", "ipv4", "Máscara", "MAC"]
        newInterface = []
        listInterface = []
        i = 0
        for interface in resp_json["ietf-interfaces:interfaces-state"]["interface"]:
            i += 1
            for addr in self.getIP(interface["name"]):
                newInterface = [
                    i,
                    interface["name"],
                    addr["ip"],
                    addr["netmask"],
                    interface["phys-address"]
                ]
                listInterface.append(newInterface)

        print(tabulate(listInterface, cabecera))

    def get_dataNetconf(self):

        m = manager.connect(
            host=self.ip,
            port=830,
            username=self.basicAuth["username"],
            password=self.basicAuth["password"],
            hostkey_verify=False
        )

        netconf_filter = """
        <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>
        """

        # using the NETCONF get method, get data:
        netconf_reply = m.get(filter=netconf_filter)

        # use the xmldict module to parse the NETCONF reply (in xml form)
        # the retuned object is a Python dictionary
        netconf_reply_dict = xmltodict.parse(netconf_reply.xml)

        netconf_reply_dict2 = netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]

        cabecera = ["Número", "Nombre", "ipv4", "Máscara", "MAC"]
        newInterface = []
        listInterface = []
        i = 0
        print(len(netconf_reply_dict2))
        try:
            for interface in netconf_reply_dict2:
                i += 1
                for addr in self.getIP(interface["name"]):
                    newInterface = [
                        i,
                        interface["name"],
                        addr["ip"],
                        addr["netmask"],
                        interface["phys-address"]
                    ]
                    listInterface.append(newInterface)
            print(tabulate(listInterface, cabecera))

        except:
            self.get_dataRestconf()


# =======================DELETE INTERFACE=============================
    def deleteInterface(self, value):

        requests.packages.urllib3.disable_warnings()

        api_url = "https://"+self.ip + \
            "/restconf/data/ietf-interfaces:interfaces/interface="+value

        resp = requests.delete(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)

        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
        else:
            print("Error code {}, reply: {}".format(
                resp.status_code, resp.json()))

# ===============================ROUTING========================
    def getRoutingData(self):

        requests.packages.urllib3.disable_warnings()
        api_url = "https://" + self.ip + \
            "/restconf/data/ietf-routing:routing-state/routing-instance"

        resp = requests.get(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)

        if(resp.status_code >= 200 and resp.status_code <= 299):
            resp_json = resp.json()
            packRoutes = resp_json["ietf-routing:routing-instance"]
            newRoute = []
            routeList = []
            cabecera = ["id", "Destination-prefix", "Outgoing-interface",
                        "Next-hop-address"]
            i = 0
            for routespack in packRoutes:

                for ribs in routespack["ribs"]["rib"]:

                    for route in ribs["routes"]["route"]:

                        nexthopaddress = "--"
                        outgoinginterface = "--"

                        if 'next-hop-address' in route["next-hop"].keys():
                            nexthopaddress = route["next-hop"]["next-hop-address"]

                        if 'outgoing-interface' in route["next-hop"].keys():
                            outgoinginterface = route["next-hop"]["outgoing-interface"]

                        newRoute = [
                            i,
                            route["destination-prefix"],
                            outgoinginterface,
                            nexthopaddress,
                        ]

                        routeList.append(newRoute)
                        i += 1

            print(tabulate(routeList, cabecera))

        else:
            print("Error code {}, reply: {}".format(
                resp.status_code, resp.json()))

    def createInterface(self, name="", description="", ip="", enabled=True, netmask="255.255.255.0", type="softwareLoopback"):

        requests.packages.urllib3.disable_warnings()

        api_url = "https://"+self.ip + \
            "/restconf/data/ietf-interfaces:interfaces/interface=" + name
        print(api_url)

        basicauth = ("cisco", "cisco123!")

        yangConfig = {
            "ietf-interfaces:interface": {
                "name": name,
                "description": description,
                "type": "iana-if-type:"+type,
                "enabled": enabled,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": ip,
                            "netmask": netmask
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        }

        print(yangConfig)

        resp = requests.put(api_url, data=json.dumps(yangConfig),
                            auth=basicauth, headers=self.headers, verify=False)
        if (resp.status_code >= 200 and resp.status_code <= 299):
            pass
        else:
            print("Error code {}, reply: {}".format(
                resp.status_code, resp.json()))

    def getCapability(self):

        api_url = "https://"+self.ip + \
            "/restconf/data/ietf-yang-library:modules-state"

        resp = requests.get(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)
        resp_json = resp.json()
        print(json.dumps(resp_json, indent=4))

        if (resp.status_code >= 200 and resp.status_code <= 299):
            pass
        else:
            print("Error code {}, reply: {}".format(
                resp.status_code, resp.json()))

    def getVersionandMemory(self):

        api_url = "https://" + self.ip + "/restconf/data/Cisco-IOS-XE-native:native/"
        api_urlMemory = "https://" + self.ip + \
            "/restconf/data/Cisco-IOS-XE-memory-oper:memory-statistics/memory-statistic"

        resp1 = requests.get(api_url, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)
        resp_json1 = resp1.json()
        version = resp_json1["Cisco-IOS-XE-native:native"]["version"]
        print("-Versión Software: ", version)
        resp2 = requests.get(api_urlMemory, auth=(
            self.basicAuth["username"], self.basicAuth["password"]), headers=self.headers, verify=False)
        resp_json2 = resp2.json()
        print("-Datos memoria:")
        for resp in resp_json2["Cisco-IOS-XE-memory-oper:memory-statistic"]:
            for key, value in resp.items():
                print("\t+"+str(key) + " --> " + str(value))
