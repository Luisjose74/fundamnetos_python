#ejercicio 

"""1. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en
dos tuplas y muestre por pantalla su producto escalar."""

vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

print("El producto escalar de los vectores es:", producto_escalar)

""""2. Escribir un programa que almacene en una lista los siguientes
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el
mayor de los precios."""

precios = [50, 75, 46, 22, 80, 65, 8]

mayor_precio = max(precios)
menor_precio = min(precios)

print("El precio mayor es:", mayor_precio)
print("El precio menor es:", menor_precio)

