#Al ejecutar el programa, solicitar al usuario sus datos de acceso (nombre de
#usuario y contraseña) y permitir visualizar el reporte siempre que los datos sean
#correctos.
#En caso de que los datos ingresados sean incorrectos, mostrar las siguientes
#opciones:
#○ Intentar nuevamente.
#○ “Añadir un nuevo usuario”.
#● Definir dentro del código al menos 4 usuarios diferentes. Respetando el
#máximo de sólo dos usuarios-administradores.
from lifestore_file import *
lusuarios=[["emtech1","caso1","admin"],["emtech2","caso2","admin"],["emtech3","caso3","usuario"],
           ["emtech4","caso4","usuario"],["emtech5","caso5","usuario"]]
bandlog=False
print(lusuarios[0][0])
print(lusuarios[0][1])
x=0
while bandlog==False:
    cusu=input("Usuario: ")
    cpass = input("Pasword: ")
    if lusuarios[x][0]==cusu and lusuarios[x][1]==cpass:
        print("entre")
        bandlog=True
    else:
        print("El usuario no existe...")
        opc1=input("Deseas intentar de nuevo o crear usuario? N para nuevo C para crear")
        if opc1=="C":
            nombre=input("nombre de usuario: ")
            passw=input("password: ")
            rol = input("rol: ")
            if rol == "admin":

            lusuarios.append([nombre,passw,rol])
            bandlog = True
        else:
            print("intentando de nuevo.")
