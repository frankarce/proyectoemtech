import csv
from operator import itemgetter
dato = []
pasajeros=[]
iata=[]
airo=[]
iata2=[]
with open('aeropuertos_pasajeros.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        dato.append(row)
dato.pop(0)
for x in dato:
    iata.append(x[2])
#'Estado', 'Ciudad', 'Codigo_IATA', 'Pasajeros', 'Vuelos_Sinaloa'
for item in iata:
    if item not in iata2:
        iata2.append(item)

for x in iata2:
    count = 0
    for y in dato:
        if x == y[2]:
            count += int(y[3])
    airo.append([x, count])
for x in dato:
    pasajeros.append(int(x[3]))
fincoru = sorted(airo, key=itemgetter(1))
bot5 = fincoru[0:5]
fincoru.reverse()
top5 = fincoru[0:5]
mean = sum(pasajeros)/len(pasajeros)
print(mean)
print("Los 5 aeropuertos con menos pasajeros a sinaloa:",bot5)
print("el promedio de pasajeros es:",mean)
print("Los 5 aeropuertos con mas pasajeros a sinaloa:",top5)
