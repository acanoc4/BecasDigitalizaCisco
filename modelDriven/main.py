from YangFunctionPackage import *

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
        print("3) Borrar Interfaces")
        print("4) Obtener la tabla de routing")
        print("5) Obtener capabilities")
        print("6) Versión y Uso de memoria")
        print("X) Pulse cualquier otra tecla para salir")

 eleccion = input("Escoja opción->")
  switcher = {

        "1": ,

        "2": ,

        "3": ,

        "4": ,

        "5": }

   try:

        switcher[eleccion]()  # para llamar a las funciones

        print("\n\n")

    except Exception as e:
        print(e)
        print("BYE BYE\n")
        break


if __name__ == "__main__":

    print("ESTABLECER LOS SIGUIENTES DATOS PARA ACCEDER AL ROUTER")

    myAccess = YangFunctionPackage(input("Introduzca IP router:"), input(
        "Introduzca usuario:"), input("Introduzca password:"))

    while True:
        if (myAccess.isValid()):
            main()
            break
        else:
            if input(
                    "Error de acceso! Quiere Volver a intentarlo?? S/N") != "S":
                break
