
#listas 

# estructura de una lista 

lista = ["objeto_1", "objeto_2", "objeto_3"]
print(type(lista)) # <class 'list'>

#listas mixtas
lista_mixta = ["Hola", 123, 3.14, True]
print(lista_mixta) # ['Hola', 123, 3.14, True]

# crear una lista de aprendices sena ADSO
# indice:       0       1        2        3         4   
aprendices = ["Juan", "Maria", "Pedro", "Luis", "Carlos"]
print (aprendices)

# acceder a un elemento de la lista 
print(aprendices[1]) # maria

#modificar un elemento de la lista
aprendices[2] = "Juana"
print(aprendices)

#consulta rango de elementos de la lista
print(aprendices[1:4]) # ['Maria', 'Pedro', 'Juana']
print(aprendices[:3]) # ['Juan', 'Maria', 'Juana']
print(aprendices[2:5]) # ['Juana', 'Luis', 'Carlos']


aprendices_ficha_3321349 = ["Ana", "Luis", "Sofia", "Diego", "Valentina"]
print(aprendices_ficha_3321349) # ['Ana', 'Luis', 'Sofia', 'Diego', 'Valentina']

aprendices_ficha_3234223 = ["Luis", "Sofia", "Diego", "Valentina"]
print(aprendices_ficha_3234223) # ['Luis', 'Sofia', 'Diego', 'Valentina', 'Andres']

# unir dos listas
aprendices_ficha_3321349.extend(aprendices_ficha_3234223)
print(aprendices_ficha_3321349) # ['Ana', 'Luis', 'Sofia', 'Diego', 'Valentina', 'Andres']

#contar el numero de elementos de una lista
aprendices_ficha_3321349 = len(aprendices_ficha_3321349)
print(f"El numero de aprendices en la ficha 3321349 es: {aprendices_ficha_3321349}") # El numero de aprendices en la ficha 3321349 es: 10

#contar el elmento count
aprendices_ficha_3321349 = ["Ana", "Luis", "Sofia", "Diego", "Valentina"]
print(aprendices_ficha_3321349.count("Luis")) # 1

#obtener el indice de un elemento
print(aprendices_ficha_3321349.index("Sofia")) # 2

#copiar una lista
nueva_lista = aprendices_ficha_3321349.copy()
print(nueva_lista) # ['Ana', 'Luis', 'Sofia', 'Diego', 'Valentina']

#agregar elementos (append y insert)
nueva_lista.append("Andres")
print(nueva_lista) # ['Ana', 'Luis', 'Sofia', 'Diego', 'Valentina', 'Andres']
nueva_lista.insert(2, "Maria")
print(nueva_lista) # ['Ana', 'Luis', 'Maria', 'Sofia', 'Diego', 'Valentina', 'Andres']

#eliminar elementos (remove y pop)
nueva_lista.remove("Maria")
print(nueva_lista) # ['Ana', 'Luis', 'Sofia', 'Diego', 'Valentina', 'Andres']
nueva_lista.pop(3)
print(nueva_lista) # ['Ana', 'Luis', 'Sofia', 'Valentina', 'Andres']    

#comprobar pertenencia (in)
if "Luis" in nueva_lista:
    print("Luis esta en la lista") # Luis esta en la lista
else:
    print("Luis no esta en la lista")
    
#ordenar una lista (sort)
nueva_lista.sort()
print(nueva_lista) # ana, andres, luis, sofia, valentina

