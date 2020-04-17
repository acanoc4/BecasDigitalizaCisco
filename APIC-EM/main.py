from tabulate import *
import json
import requests
from APIC_ticket import *
from APICEMFunctionPack import *


APICEM_DATA = {
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
    username = input("Introduzca username->")
    password = input("Introduzca password->")
    api_url = input(
        "Introduzca URL (Ejemplo:https://DevnetSBX-NetAcad-APICEM-3.cisco.com)->")

    APICEM_DATA["username"] = username
    APICEM_DATA["password"] = password
    APICEM_DATA["api_url"] = api_url


def setDefaultCredential():
    pass


def getNetworkHostInventory():
    get_NetworkHostInventory(APICEM_DATA["api_url"], APICEM_DATA["key"])


def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~ Bienvedio al controlador APIC-EM! ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    while True:
        print("=====================================")
        print("========>    MENÚ APIC-EM    <=======")
        print("=====================================")

        print("1) Listar los Host de la red")
        print("2) Usar credenciales y URL por defecto")
        print("3) Listar los Host de la red")
        print("X) Pulse cualquier otra tecla para salir")

        eleccion = input("Escoja opción->")
        switcher = {

            "1": getNetworkHostInventory,

            "2": "xxx",
        }

        try:

            switcher[eleccion]()  # para llamar a las funciones

            print("\n\n")

        except:
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
