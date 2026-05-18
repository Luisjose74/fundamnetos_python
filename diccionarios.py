#diccionarios (caractiristicas a un elemento)

# creacion de un diccionario


#estructura de un diccionario 
diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}
print(type(diccionario)) # <class 'dict'>


#Diccionario vacio 
diccionario_vacio = {}
print(type(diccionario_vacio)) # <class 'dict'>

#diccionario con elementos 

diccionario_aprendiz = {
    "Nombre": "Juan",
    "Apellido": "Perez",
    "programa": "ADSO",
    "Edad": 30,
    "Ciudad": "Bogota"
}

print(type(diccionario_aprendiz))


#obtener un valor del diccionario 
print(diccionario_aprendiz["Ciudad"])
print(diccionario_aprendiz.get("Ciudad"))

#obtener solo las claves
print(diccionario_aprendiz.keys())

#obtener solo los valores
print(diccionario_aprendiz.values())

#obtener las claves y los valores
print(diccionario_aprendiz.items()) 

#agregar un elemento al diccionario
diccionario_aprendiz["Telefono"] = "123456789"
print(diccionario_aprendiz)

#modificar un elemento del diccionario
diccionario_aprendiz["Telefono"] = "987654321"
print(diccionario_aprendiz)

#metodo update
diccionario_aprendiz.update({"Nomnbre": "Maria"})
diccionario_aprendiz.update({"Apellido": "Lopez"})
print(diccionario_aprendiz)

#comprobar pertenencia (in)
if "Telefono" in diccionario_aprendiz:
    print("Telefono pertenece al diccionario")
else:
    print("Telefono no pertenece al diccionario")
    
#recorrer solo claves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave)

#recorrer solo valores del diccionario
for valor in diccionario_aprendiz.values():
    print(valor)
    
#recorrer claves y valores del diccionario
for clave, valor in diccionario_aprendiz.items():
    print(clave, valor)

#eliminar un elemento del diccionario pop()
diccionario_aprendiz.pop("Telefono")
print(diccionario_aprendiz)

#eliminar todos los elemento del diccionario clear()
diccionario_aprendiz.clear()
print(diccionario_aprendiz)

# diccionario anidados 

aprendiz_1 = {
    "Nombre": "luis",
    "Apellido": "silva",
    "programa": "ADSO",
    "Edad": 22,
    "Ciudad": "Bogota"
}

aprendiz_2 = {
    "Nombre": "Maria",
    "Apellido": "Lopez",
    "programa": "ADSO",
    "Edad": 20,
    "Ciudad": "Bogota"
}

aprendiz_3 = {
    "Nombre": "Pedro",
    "Apellido": "Perez",
    "programa": "ADSO",
    "Edad": 24,
    "Ciudad": "Bogota"
}

diccionario_aprendizes = {
    "aprendiz_1": aprendiz_1,
    "aprendiz_2": aprendiz_2,
    "aprendiz_3": aprendiz_3
}

print(diccionario_aprendizes)

#recorrer un diccionario anidados con un ciclo for 

for aprendiz in diccionario_aprendiz.items():
    print(f"{aprendiz}:")
    for clave, valor in aprendiz.items():
        print(f"{clave}: {valor}")

