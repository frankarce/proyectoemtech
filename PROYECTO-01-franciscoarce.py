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
from datetime import date, time, datetime
lusuarios=[["emtech1","caso1","admin"],["2","2","admin"],["emtech3","caso3","usuario"],
           ["emtech4","caso4","usuario"],["emtech5","caso5","usuario"]]
bandlog=False
print(lusuarios[0][0])
print(lusuarios[0][1])
x=0
while bandlog==False:
    cusu=input("Usuario: ")
    cpass = input("Pasword: ")
    print(x)
    if lusuarios[x][0]==cusu and lusuarios[x][1]==cpass:
        bandlog=True
    else:
        print("El usuario no existe...")
        opc1=input("Deseas intentar de nuevo o crear usuario? N para nuevo C para crear")
        if opc1=="C":
            nombre=input("nombre de usuario: ")
            passw=input("password: ")
            lusuarios.append([nombre,passw,"usuario"])
            bandlog = True
        else:
            print("intentando de nuevo.")
            x=x+1

listaventas=[0]*97
for x in range(len(lifestore_sales)):
    #print("soy x:",x)
    #print(lifestore_sales[x][1])
    for y in range (len(lifestore_products)):
        #print("soy y:", y)
        #print(lifestore_products[y][0])
        if lifestore_sales[x][1]==lifestore_products[y][0]:
            listaventas[y]=listaventas[y]+1
listaventastop5=listaventas
listaventasnotop5=listaventas
top5vent=[]
notop5vent=[]
for r in range(5):
    d=max(listaventastop5)
    top5vent.append([listaventastop5.index(d)+1,d])
    listaventastop5.pop(listaventastop5.index(d))
print("Generar un listado de los 5 productos con mayores ventas donde [id prod, cantidad]")
print(top5vent)
for t in range(5):
    k=min(listaventasnotop5)
    #print(k)
    #print(listaventasnotop5.index(k)+1)
    notop5vent.append([listaventasnotop5.index(k)+1,k])
    listaventasnotop5.pop(listaventasnotop5.index(k))
print("Generar un listado de los 5 productos con menores ventas, como hace pop al elemento a verificar se repite el elemento 11 al tomar el espacio del eliminado donde [id prod, cantidad]")
print(notop5vent)

listabusquedas=[0]*97
for x in range(len(lifestore_searches)):
    #print("soy x:",x)
    #print(lifestore_sales[x][1])
    for y in range (len(lifestore_products)):
        #print("soy y:", y)
        #print(lifestore_products[y][0])
        if lifestore_searches[x][1]==lifestore_products[y][0]:
            listabusquedas[y]=listabusquedas[y]+1
print(listabusquedas)
listabusquedastop10=listabusquedas
listabusquedasnotop10=listabusquedas
top10bu=[]
notop10bu=[]
for q in range(10):
    p=max(listabusquedastop10)
    top10bu.append([listabusquedastop10.index(p)+1,p])
    listabusquedastop10.pop(listabusquedastop10.index(p))
print("Generar un listado de los 10 productos mas buscados [id prod, cantidad]")
print(top10bu)
for e in range(10):
    b=min(listabusquedasnotop10)
    notop10bu.append([listabusquedasnotop10.index(b)+1,b])
    listabusquedasnotop10.pop(listabusquedasnotop10.index(b))
print("Generar un listado de los 10 productos menos buscados [id prod, cantidad]")
print(notop10bu)
lre=[0]*97
for x in range(len(lifestore_sales)):
    #print("soy x:",x)
    #print(lifestore_sales[x][1])
    for y in range (len(lifestore_products)):
        #print("soy y:", y)
        #print(lifestore_products[y][0])
        if lifestore_sales[x][1]==lifestore_products[y][0]:
            lre[y]=lre[y]+lifestore_sales[x][2]
lre5=lre
nolre5=lre
top5re=[]
for s in range(5):
    w=max(lre5)
    top5re.append([lre5.index(w)+1,w])
    lre5.pop(lre5.index(w))
print("Generar un listado de los 5 productos mejor  rankeados [id prod, cantidad]")
print(top5re)
notop5re=[]
for u in range(5):
    i=min(nolre5)
    notop5re.append([nolre5.index(i)+1,i])
    nolre5.pop(nolre5.index(i))
print("Generar un listado de los 5 productos peor  rankeados [id prod, cantidad]")
print(notop5re)

lvt=[0]*97
for x in range(len(lifestore_sales)):
    #print("soy x:",x)
    #print(lifestore_sales[x][1])
    for y in range (len(lifestore_products)):
        #print("soy y:", y)
        #print(lifestore_products[y][0])
        if lifestore_sales[x][1]==lifestore_products[y][0]:
            lvt[y]=lvt[y]+(lifestore_sales[x][2])
print(listabusquedas)
