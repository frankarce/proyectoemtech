idprod=0
venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
maiz=0
tomate=0
pep=0
idprod=int(input("Ingresa el ID del producto: "))
for x in range(len(venta_productos)):
if venta_productos[x][0]==1:
maiz=maiz+venta_productos[x][1]
if venta_productos[x][0] == 2:
pep=pep + venta_productos[x][1]
if venta_productos[x][0] == 3:
tomate = tomate+venta_productos[x][1]

if idprod==1:
print("El producto es Maiz de Grano")
print("El precio por caja es: $285.55")

if maiz<1500:
    print("Aplicar el descuento de 20%: ",True)
    total=(maiz*285.55)
    print(total)
    print("El precio total a pagar es :",total*285.55)
else:
    print("Aplicar el descuento de 20%: ", False)
    print("El precio total a pagar es :", maiz * 285.55)
elif idprod==2:

if pep < 1500:
    print("Aplicar el descuento de 20%: ", True)
    total = (pep * 334.72) - (0.2 * (pep * 334.72))
    print("El precio total a pagar es :", total * 285.55)
else:
    print("Aplicar el descuento de 20%: ", False)
    print("El precio total a pagar es :", maiz * 285.55)
elif idprod==3:
if tomate < 1500:
print("Aplicar el descuento de 20%: ", True)
total = (pep * 334.72) - (0.2 * (pep * 334.72))
print("El precio total a pagar es :", total * 285.55)
else:
print("Aplicar el descuento de 20%: ", False)
print("El precio total a pagar es :", tomate * 285.55)
else:
print("El producto no existe")
