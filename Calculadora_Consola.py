#ELIAS MAMANI CALAMANI

#Funciones de operaciones
def Sumar(a,b):
    print('r=',a+b)

def Restar(a,b):
    print('r=', a - b)

def Multiplicar(a,b):
    print('r=', a * b)

def Dividir(a,b):
    print('r=', a / b)
def menuInterfaz():
    print('******* *menu*********')
    print('* 1. Sumar           *')
    print('* 2. Restar          *')
    print('* 3. Multiplicar     *')
    print('* 4. Dividir         *')
    print('** Elija una opción **')

#programa menu
while True:
    menuInterfaz()
    opcion = int(input(':'))
    if opcion == 1:
        Sumar(float(input('a=')),float(input('b=')))
    elif opcion == 2:
        Restar(float(input('a=')), float(input('b=')))
    elif opcion == 3:
        Multiplicar(float(input('a=')), float(input('b=')))
    elif opcion == 4:
        Dividir(float(input('a=')), float(input('b=')))
    else:
        break