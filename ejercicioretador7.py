#############Seccion de solicitud de datos
#EJERCICIO RETADOR #7
from operator import itemgetter
pasajeros = []
opt="5"
def captura():
    x = "si"

    while x == "si":
        IDE= input("Ingresa el IFE/INE: ")
        nom = input("Ingresa el nombre: ")
        eda = int(input("Ingresa la edad: "))
        IATA = input("Ingresa el destino: ")
        CPT = input("Es Cliente Preferente si/no: ")
        if CPT=="si":
            CP=True
        elif CTP == "no":
            CP = False
        else:
            False
        Dic={'ide':IDE,'nom':nom,'eda':eda,'IATA':IATA,'CP':CP}
        pasajeros.append(Dic)
        x=input("desea capturar otro si/no:")
def todos():
    for x in pasajeros:
        print(x['IDE'],x['nom'])
def CP():
    for x in (pasajeros):
        if x['CP']==True:
            print(x['IDE'], x['nom'])

while opt != "4":
    print("***********************Menu*******************")
    print("1.- Capturar Cliente.")
    print("2.- Mostrar Clientes.")
    print("3.- Mostrar Clientes Preferentes.")
    print("4. Salir")
    opt=input("Elige una opcion:")
    if opt=="1":
        captura()
    if opt=="2":
        todos()
    if opt=="3":
        CP()
    if opt=="4":
        print("Adios...")
