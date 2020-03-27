#Calculadora
from math import sqrt


def suma():
    try:
        num1 = float(input("Introduzca el primer dígito:"))
        num2 = float(input("Introduzca el segundo dígito:"))
        print(num1,"+",num2,"=",num1+num2)
    except:
        print("ERROR DURANTE LA SUMA!")

def resta():
    try:
        num1 = float(input("Introduzca el primer dígito:"))
        num2 = float(input("Introduzca el segundo dígito:"))
        print(num1,"-",num2,"=",num1-num2)
    except:
        print("ERROR DURANTE LA RESTA!")

def multiplicacion():
    try:
        num1 = float(input("Introduzca el primer dígito:"))
        num2 = float(input("Introduzca el segundo dígito:"))
        print(num1,"*",num2,"=",num1*num2)
    except:
        print("ERROR DURANTE LA MULTIPLICACIÓN!")

def division():
    try:
        num1 = float(input("Introduzca el primer dígito:"))
        num2 = float(input("Introduzca el segundo dígito:"))
        print(num1,"/",num2,"=",num1/num2)
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR ENTRE 0!")
    except:
        print("ERROR DURANTE LA MULTIPLICACIÓN!")

def exponenciacion():
    try:
        num1 = float(input("Introduzca el primer dígito:"))
        num2 = float(input("Introduzca el segundo dígito:"))
        assert not(num1==0 and num2<=0)
        print(num1,"^",num2,"=",num1**num2)
        

    except AssertionError:
        if(num2==0):
            print("Indeterminación!!!")
        else:
            print("INFINITO!!!")
    except:
        print("ERROR DURANTE LA POTENCIA!")

def raices():
    try:
        num1 = float(input("Introduzca el dígito:"))
        assert num1>=0
        print(num1,"^(1/2)=",num1**(1/2))
        
    except AssertionError:
        print("ES UN NÚMERO IMAGINARIO!!!")
    except:
        print("ERROR DURANTE LA MULTIPLICACIÓN!")




switcher = {
    "1":suma,
        
    "2":resta,
        
    "3":multiplicacion,

    "4":division,

    "5":exponenciacion,
        
    "6":raices
}




while True:
        
    print("**"*5+"Menú"+"**"*5)
    print("Seleccione Operación.")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplación")
    print("4.División")
    print("5.Exponencial")
    print("6.Raíces Cuadradas")
    print("Otro. Salir")

    eleccion = input("Escriba el número de operación-> ")


    try:
            
            switcher[eleccion]()#para llamar a las funciones

            print("\n\n")

    except:
        print("BYE BYE\n")
        break
