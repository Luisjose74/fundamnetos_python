#tuplas 

#estructura de una tupla
#indice:      0           1           2
tupla = ("objeto_1", "objeto_2", "objeto_3") 
print(type(tupla)) # <class 'tuple'>

tupla_2 = "a", "b", "c" 
print(type(tupla_2)) # <class 'tuple'>

tupla_3 = ("a",) # para crear una tupla de un solo elemento, se debe agregar una coma al final
print(type(tupla_3)) # <class 'tuple'>

tupla_4 = tuple("hola") # para crear una tupla a partir de una cadena
print(type(tupla_4)) # <class 'tuple'>

tuple_mixta = ("hola", 123, 3.14, True)
print(tuple_mixta) # ('hola', 123, 3.14, True)

# tuple de aprendices sena ADSO

# indice:       0       1         2       3         4   
aprendices = ("Juan", "Maria", "Pedro", "Luis", "Carlos")
print (aprendices)

# acceder a un elemento de la tupla
print(aprendices[1]) # maria

#modificar un elemento de la tupla
# aprendices[2] = "Juana"
# print(aprendices) # TypeError: 'tuple' object does not support item assignment

#consulta rango de elementos de la tupla
print(aprendices[1:4]) # ('Maria', 'Pedro', 'Luis')
print(aprendices[:3]) # ('Juan', 'Maria', 'Pedro')
print(aprendices[2:5]) # ('Pedro', 'Luis', 'Carlos')

#sumar 2 tuplas
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_3 = tupla_1 + tupla_2
print(tupla_3) # (1, 2, 3, 4, 5, 6)

#multiplicar una tupla
tupla_4 = tupla_1 * 3
print(tupla_4) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

#medir la longitud de una tupla
aprendices = (1, 2, 3, 4, 5, 6)
print(len(aprendices)) # 6


#contar elementos repetidos
aprendices = ("Juan", "Maria", "Pedro", "Luis", "Carlos", "Maria")
print(aprendices.count("Maria")) # 2

# modificar una tupla en una lista 

aprendices_lista = list(aprendices) # convertir una tupla en una lista
print(aprendices_lista) # ['Juan', 'Maria', 'Pedro', 'Luis', 'Carlos', 'Maria']

aprendices_lista[2] = "Juana" # modificar un elemento de la lista
print(aprendices_lista) # ['Juan', 'Maria', 'Juana', 'Luis', 'Carlos', 'Maria']

aprendices = tuple(aprendices_lista) # convertir una lista en una tupla
print(aprendices) # ('Juan', 'Maria', 'Juana', 'Luis', 'Carlos', 'Maria')

#comprobar pertenencia
print("Maria" in aprendices) # True
print("Pedro" in aprendices) # False

#empaquetar tuplas 

programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "TOPOGRAFIA"

tupla_programa = programa_1, programa_2, programa_3
print(tupla_programa) # ('ADSO', 'SST', 'TOPOGRAFIA')

#desempaquetar tuplas 

programa_1, programa_2, programa_3 = tupla_programa
print(programa_1) # ADSO
print(programa_2) # SST
print(programa_3) # TOPOGRAFIA

#ejercio 2 desquempaquetar tuplas 

tupla_cuidades = ("bogota", "medellin", "cali", "barranquilla", "cartagena")

ciudad_1, ciudad_2, ciudad_3, ciudad_4, ciudad_5 = tupla_cuidades

print(ciudad_1) # bogota
print(ciudad_2) # medellin
print(ciudad_3) # cali
print(ciudad_4) # barranquilla
print(ciudad_5) # cartagena

#iterar sobre una tupla con ciclo for
for ciudad in tupla_cuidades: # para recorrer una tupla 
    print(ciudad) 




