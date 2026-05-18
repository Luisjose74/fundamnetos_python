#conjuntos (sets) en python 

# estructura de un conjunto

conjunto = set()
print(type(conjunto)) # <class 'set'>

# creacion

leguajes = {"python", "java", "c++", "c#"}
print(leguajes) # <class 'set'>

# --- Metodos de modificacion --- 
frutas = {"manzana", "pera", "banana"} # conjunto
frutas.add("naranja") # agrega un elemento al conjunto
frutas.remove("pera") # elimina; keyError si no existe
frutas.discard("banana") # elimina; No lanza error si no existe
elemento = frutas.pop() # elimina un elemento al azar
print(frutas)

# --- vereficar pertencia: 0(1) ---
print("manzana" in frutas) # True
print("pera" in frutas) # False

python_devs = {"Juan", "luis", "Pedro", "Maria", "Carlos"}
java_devs = {"Luis", "Maria", "oscar", "pedro", "kevin"}


#union de conjuntos

devs = python_devs | java_devs
print(devs) # {'Juan', 'Pedro', 'Maria', 'Carlos', 'Luis', 'oscar', 'kevin'}

#interseccion de conjuntos

devs = python_devs & java_devs
print(devs) # {'Maria', 'Pedro'}

#diferencia de conjuntos

devs = python_devs - java_devs
print(devs) # {'Juan', 'Carlos'}

devs = java_devs - python_devs
print(devs) # {'Luis', 'oscar', 'kevin'}

#diferencia simetrica de conjuntos

devs = python_devs ^ java_devs
print(devs) # {'Juan', 'Pedro', 'Carlos', 'Luis', 'oscar', 'kevin'}
