#############Seccion de solicitud de datos
#EJERCICIO RETADOR #7
from operator import itemgetter
edatp=[]
edacp=[]
pasajeros = {"45471":["Luis Perez",45,"BJX", True], "8944411":["FernandaGarcia",25,"JAL", True],"15223":["Alejandra Ortiz",33,"JDL", True]}
opt="5"
def agregarClientes():
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
        Dic={IDE:[nom,eda,IATA,CP]}
        pasajeros.update(Dic)
        x=input("desea capturar otro si/no:")
def todos():
    for x in pasajeros:
        print(x['IDE'],x['nom'])
def CP():
    for x in (pasajeros):
        if x['CP']==True:
            print(x['IDE'], x['nom'])
def eliminarClientes():
    c=" "
    while c != "no":
        idife = input("Ingresa el id para eliminar")
        for x in pasajeros:
            if x["ide"][0]==idife:
                pasajeros.pop(idlife)
    x = input("desea capturar otro si/no:")
    return
def edadpromedio():
    for clave, valor in pasajeros.items():
        edatp.append(valor[1])
        if valor==False:
            edacp.append(valor[1])
    print("Promedio de todas las edades de los clientes:",sum(edatp) / len(edatp))
    print("Promedio de todas las edades de los clientes preferentes:", sum(edatp) / len(edatp))

    return
while opt != "4":
    print("***********************Menu*******************")
    print("1.- Capturar Cliente.")
    print("2.- Mostrar Clientes.")
    print("3.- Mostrar Clientes Preferentes.")
    print("4.- Eliminar cliente")
    print("5.- Edad Promedio")
    print("6.- Salir")
    opt=input("Elige una opcion:")
    if opt=="1":
        agregarClientes()
    if opt=="2":
        todos()
    if opt=="3":
        CP()
    if opt == "4":
        eliminarClientes()
    if opt == "5":
        edadpromedio()
    if opt=="6":
        print("Adios...")
