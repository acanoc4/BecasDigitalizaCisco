
from functionPackage import YangFunctionPackage


def get_dataNetconf():
    myAccess.get_dataNetconf()


def get_dataRestconf():
    myAccess.get_dataRestconf()


def deleteInterface():
    myAccess.deleteInterface(
        input("Escriba el nombre de la interfaz a eliminar:"))


def getRoutingData():
    myAccess.getRoutingData()


def createInterface():
    name = input("Escriba el nombre de la interfaz:")
    description = input("Escriba descripcion de la interfaz:")
    ip = input("Escriba ip de la interfaz:")
    netmask = input("Escriba máscara de la interfaz:")
    tipo = input("Escriba el tipo de la interfaz ejm (softwareLoopback):")
    myAccess.createInterface(name=name, description=description,
                             ip=ip, enabled=True, netmask=netmask, type=tipo)


def getCapability():
    myAccess.getCapability()


def getVersionandMemory():
    myAccess.getVersionandMemory()


myAccess = ""


def main():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~   Bienvedio al Router csr1000v!   ~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")

    while True:
        print("=====================================")
        print("========>        MENÚ        <=======")
        print("=====================================")

        print("1) Obtener listado de las interfaces Restconf")
        print("2) Obtener listado de las interfaces Netconf")
        print("3) Crear Interfaces")
        print("4) Borrar Interfaces")
        print("5) Obtener la tabla de routing")
        print("6) Obtener librerías yang")
        print("7) Versión y Uso de memoria")
        print("X) Pulse cualquier otra tecla para salir")

        eleccion = input("\nEscoja opción->")
        switcher = {

            "1": get_dataRestconf,

            "2": get_dataNetconf,

            "3": createInterface,

            "4": deleteInterface,

            "5": getRoutingData,

            "6": getCapability,

            "7": getVersionandMemory}

        try:

            switcher[eleccion]()  # para llamar a las funciones

            print("\n\n")

        except Exception as e:
            print(e)
            print("BYE BYE\n")
            break


if __name__ == "__main__":

    print("ESTABLECER LOS SIGUIENTES DATOS PARA ACCEDER AL ROUTER")

    while True:
        myAccess = YangFunctionPackage(input("Introduzca IP router:"), input(
            "Introduzca usuario:"), input("Introduzca password:"))
        if (myAccess.isValid()):
            main()
            break
        else:
            if input(
                    "Error de acceso! Quiere Volver a intentarlo?? S/N: ") != "S":
                break
