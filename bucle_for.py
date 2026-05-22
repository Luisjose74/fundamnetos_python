# Bucle For = instruccion de control que se repite numero determinado de veces

lenguaje = "Python"

for letra in lenguaje:
    print(letra)
    
frutas = ["Manzana", "Banana", "naranja"]

# recorre todos los elementos de la lista Frutas
for fruta in frutas:
    if fruta == "Banana":
        break # para romper la sentencia o que pare.
    print(fruta)
    
    # recorre todos los elementos de la lista Frutas
for fruta in frutas:
    if fruta == "Manzana":
        continue # Para saltar una iteracion 
    print(fruta)
    
    
    # recorre todos los elementos de la lista Frutas
for fruta in frutas:
    if fruta == "Manzana":
        continue # Para saltar una iteracion 
    print(fruta)
else:
    print("Ya se recorrieron todas las frutas")    
    
# Recorrer rangos especificos

for i in range(5): # reccorre un rango de 0 hasta el 4
    print(i)    
for i in range(2, 5): # reccorre un rango de 2 hasta el 4 por que el 5 no lo cuenta
    print(i)    
    
    
# Funcion pass para omitir o saber despues que colocar, la funcion solo es dejar pasar no hace nada
for fruta in frutas:
    if fruta == "Manzana":
        pass
    print(fruta)
    
    
#se puede recorrer una tupla con un bucle for

colores = ("azul", "rojo", "verde")

for color in colores:
    print(color)
    
#Recorrer un diccionario con bucle for

diccionario_aprendices = {"nombre":"felipe","edad": 32, "ciudad": "duitama"}
# se recorre la calve y el valor del diccionario_aprendices
for clave, valor in diccionario_aprendices.items():
    print(f"la clave es : {clave}, y su valor es: {valor}")