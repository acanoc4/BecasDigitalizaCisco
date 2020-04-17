import json
import requests


# Es de tipo singleton


class APICEM_ticket:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if APICEM_ticket.__instance == None:
            raise Exception(
                "This is the first Instance use firstInstance method")
        return APICEM_ticket.__instance

    @staticmethod
    def firstInstance(username, password, api_url):
        """ Static access method. """
        if APICEM_ticket.__instance == None:
            APICEM_ticket(username, password, api_url)
        return APICEM_ticket.__instance

    def __init__(self, username, password, api_url):
        """ Virtually private constructor. """
        if APICEM_ticket.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.ticket = self.create_ticket(username, password, api_url)
            self.username = username
            self.password = password
            self.api_url = api_url
            APICEM_ticket.__instance = self

    def create_ticket(self, username, password, api_url):
        try:
            print("Pidiendo ticket, por favor espere...")
            requests.packages.urllib3.disable_warnings()
            api_url = api_url + "/api/v1/ticket"
            headers = {
                "content-type": "application/json"
            }
            body_json = {
                "username": str(username),
                "password": str(password)
            }

            resp = requests.post(api_url, json.dumps(body_json),
                                 headers=headers, verify=False)

            response_json = resp.json()
            serviceTicket = response_json["response"]["serviceTicket"]

            response_json = resp.json()
            serviceTicket = response_json["response"]["serviceTicket"]

            return serviceTicket

        except:

            if(resp.status_code == 401):
                print("Error en el Login")
                return "-1"

    def refreshTicket(self):
        self.ticket = self.create_ticket(
            self.username, self.password, self.api_url)
        return self.ticket

    def get_ticket(self):
        return self.ticket

    def set_password(self, password):
        self.password = password

    def set_apiurl(self, api_url):
        self.api_url = api_url

    def set_username(self, username):
        self.username = username
