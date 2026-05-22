#funcion: bloque de codigo que se puede reutilizar
#definir una funcion
def nombre_funcion():
    print("Hola Mundo")

#llamar a la funcion
nombre_funcion()

#funcion con parametros
def saludar(nombre):
    return f"Hola {nombre}"

print(saludar("Juan"))
print(saludar("Maria"))
print(saludar("Pedro"))

# operaciones matematicas con funciones

def sumar(a, b):
    suma = a + b
    return suma


print(sumar(5, 3))
print(sumar(10, 20))

def restar(a, b):
    resta = a - b
    return resta

print(restar(5, 3))
print(restar(10, 20))

#ejercicio para validar edad}

def validar_edad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

edad = int(input("Ingrese su edad: "))
print(validar_edad(edad))

#usuarios sena sofis plus

aprendices = ["Juan", "Maria", "Pedro", "Ana", "Luis"]

#funcion para mostrar los aprendices
def mostrar_aprendices(aprendices):
    print("Los aprendices son: ")
    for aprendiz in aprendices:
        print(aprendiz)

mostrar_aprendices(aprendices)

#funcion para agregar aprendices
def agregar_aprendiz(aprendices, aprendiz):
    aprendices.append(aprendiz)
nuevo_aprendiz = input("Ingrese el nombre del nuevo aprendiz: ")
agregar_aprendiz(aprendices, nuevo_aprendiz)
mostrar_aprendices(aprendices)

#funcion para modificar aprendices
def modificar_aprendiz(aprendices, indice, nuevo_nombre):
    aprendices[indice] = nuevo_nombre
modificar_aprendiz(aprendices, 2, "Juana")
mostrar_aprendices(aprendices)

#funcion para eliminar aprendices
def eliminar_aprendiz(aprendices, aprendiz):
    aprendices.remove(aprendiz)
eliminar_aprendiz(aprendices, "Ana")
mostrar_aprendices(aprendices)

