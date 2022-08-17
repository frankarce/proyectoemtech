#
from operator import itemgetter
import csv
lusuarios=[["emtech1","caso1","admin"],["2","2","admin"],["emtech3","caso3","usuario"],
           ["emtech4","caso4","usuario"],["emtech5","caso5","usuario"]]
bandlog=False
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
#Columnas
#0 register_id
#1 direction
#2 origin
#3 destination
#4 year
#5 date
#6 product
#7 transport_mode
#8 company_name
#9 total_value

#

item = []
dato = []
with open('database.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        dato.append(row)
ruta = []
result = []
#funcionamos la columna origen con destino para generar la ruta
for item in dato:
    ruta.append(item[2]+item[3])
result = []
ruta.pop(0)
#Sacamos una lista de las rutas unicas para hacer conteos
for item in ruta:
    if item not in result:
        result.append(item)
coru = []
for x in result:
    count = 0
    for y in ruta:
        if x == y:
            count += 1
    coru.append([x, count])
fincoru = sorted(coru, key=itemgetter(1))
fincoru.reverse()
top10 = fincoru[0:10]
print("Las 10 rutas mas utilizadas: ")
print(top10)
