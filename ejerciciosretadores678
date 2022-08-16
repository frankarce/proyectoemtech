#############Seccion de solicitud de datos
from operator import itemgetter

x = False
pasajeros = 0
dest1, dest2, dest3 = 0, 0, 0
prom1, prom2, prom3 = [], [], []
lito = []
lito3 = []
pasajero = []
while x == False:

    nom = input("Ingresa el nombre: ")
    if nom == "X":
        break
    eda = int(input("Ingresa la edad: "))
    IATA = input("Ingresa el destino: ")
    tup = (nom, eda, IATA)
    pasajero.append(tup)

for x in pasajero:
    if x[2] == "BJX":
        dest1 = dest1 + 1
        prom1.append(x[1])
    if x[2] == "GDL":
        dest2 = dest2 + 1
        prom2.append(x[1])
    if x[2] == "JAL":
        dest3 = dest3 + 1
        prom3.append(x[1])
dv1 = ("BJX", dest1)
dv2 = ("GDL", dest2)
dv3 = ("JAL", dest3)
lito.append(dv1)
lito.append(dv2)
lito.append(dv3)
lito2 = sorted(lito, key=itemgetter(1), reverse=True)
m1 = sum(prom1) / len(prom1)
m2 = sum(prom2) / len(prom2)
m3 = sum(prom3) / len(prom3)
po1 = ("BJX", m1)
po2 = ("GDL", m2)
po3 = ("JAL", m3)
lito3.append(po1)
lito3.append(po2)
lito3.append(po3)
print(lito2)
print(lito3)
#EJERCICIO RETADOR #6
