from tabulate import *
import json
import requests
from APIC_ticket import *
from APICEMFunctionPack import *
import ipaddress


APICEM_DATA = {
    "username": "devnetuser",
    "password": "Xj3BDqbU",
    "api_url": "https://DevnetSBX-NetAcad-APICEM-3.cisco.com",
    "key": "-1"
}
APICEM_DATA_BCKUP = {
    "username": "devnetuser",
    "password": "Xj3BDqbU",
    "api_url": "https://DevnetSBX-NetAcad-APICEM-3.cisco.com",
    "key": "-1"
}


def setCredential():
    username = input("Introduzca username->")
    password = input("Introduzca password->")

    APICEM_DATA["username"] = username
    APICEM_DATA["password"] = password


def setCredentialURL():
    api_url = input(
        "Introduzca URL\n(Ejemplos:https://DevnetSBX-NetAcad-APICEM-3.cisco.com ; https://sandboxapicem.cisco.com)->")
    username = input("Introduzca username->")
    password = input("Introduzca password->")

    APICEM_DATA["username"] = username
    APICEM_DATA["password"] = password
    APICEM_DATA["api_url"] = api_url


def changeURL():
    APICEM_DATA_BCKUP["username"] = APICEM_DATA["username"]
    APICEM_DATA_BCKUP["password"] = APICEM_DATA["password"]
    APICEM_DATA_BCKUP["api_url"] = APICEM_DATA["api_url"]
    setCredentialURL()
    try:
        obj = APICEM_ticket.getInstance()
        ticket = obj.newConnection(APICEM_DATA["username"],
                                   APICEM_DATA["password"],
                                   APICEM_DATA["api_url"])

        if (str(ticket) != "-1"):
            APICEM_DATA["key"] = ticket
            print("Ticket generado!!!")
        else:
            print("Error durante el login, volviendo a anteriores credenciales...")
            APICEM_DATA["username"] = APICEM_DATA_BCKUP["username"]
            APICEM_DATA["password"] = APICEM_DATA_BCKUP["password"]
            APICEM_DATA["api_url"] = APICEM_DATA_BCKUP["api_url"]
            obj = APICEM_ticket.getInstance()
            ticket = obj.newConnection(APICEM_DATA["username"],
                                       APICEM_DATA["password"],
                                       APICEM_DATA["api_url"])
    except Exception as e:
        print(e)
        print("Error durante el acceso a la página, volviendo a anteriores credenciales...")
        APICEM_DATA["username"] = APICEM_DATA_BCKUP["username"]
        APICEM_DATA["password"] = APICEM_DATA_BCKUP["password"]
        APICEM_DATA["api_url"] = APICEM_DATA_BCKUP["api_url"]
        obj = APICEM_ticket.getInstance()
        ticket = obj.newConnection(APICEM_DATA["username"],
                                   APICEM_DATA["password"],
                                   APICEM_DATA["api_url"])


def setDefaultCredential():
    pass


def getNetworkHostInventory():
    get_NetworkHostInventory(APICEM_DATA["api_url"], APICEM_DATA["key"])


def getIPGeolocation():
    ip = input("Introduzca la dirección ip pública deseada:")

    try:
        if ipaddress.ip_address(ip).is_global:
            get_IPGeolocation(APICEM_DATA["api_url"],
                              APICEM_DATA["key"], ip)
        else:
            print("No es un IP pública")

    except:
        print("La IP escrita es errónea:" + ip)


def getFlowAnalysis():
    get_FlowAnalysis(APICEM_DATA["api_url"], APICEM_DATA["key"])


def getInterfaces():
    get_Interfaces(APICEM_DATA["api_url"],
                   APICEM_DATA["key"])


def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~ Bienvedio al controlador APIC-EM! ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    while True:
        print("=====================================")
        print("========>    MENÚ APIC-EM    <=======")
        print("=====================================")

        print("1) Listar los Host de la red")
        print("2) Conocer la Geolocalización de una IP Pública")
        print("3) Listar el flujo de tráfico")
        print("4) Listar interfaces")
        print("5) Cambiar URL y usuario")
        print("X) Pulse cualquier otra tecla para salir")

        eleccion = input("Escoja opción->")
        switcher = {

            "1": getNetworkHostInventory,

            "2": getIPGeolocation,

            "3": getFlowAnalysis,

            "4": getInterfaces,

            "5": changeURL}

        try:

            switcher[eleccion]()  # para llamar a las funciones

            print("\n\n")

        except Exception as e:
            print(e)
            print("BYE BYE\n")
            break


if __name__ == "__main__":

    print("ESTABLECER CREDENCIALES PARA ACCEDER APIC-EM")
    print("Menú LOGIN APIC-EM:")
    print("1) Logearse en url por defecto")
    print("2) Logearse en url nueva")
    print("3) Emplear Login guardada y url por defecto")
    print("X) Pulse cualquier otra tecla para salir")

    eleccion = input("Escoja opción->")

    switcher = {
        "1": setCredential,

        "2": setCredentialURL,

        "3": setDefaultCredential,
    }

    switcher[eleccion]()  # para llamar a las funciones
    print("\n\n")

    try:
        apicObj = APICEM_ticket.firstInstance(APICEM_DATA["username"],
                                              APICEM_DATA["password"],
                                              APICEM_DATA["api_url"])
        ticket = apicObj.get_ticket()
        APICEM_DATA["key"] = ticket
        if (str(ticket) != "-1"):
            print("Ticket generado!!!")
            main()
    except:
        print("Error durante el acceso a la página")
