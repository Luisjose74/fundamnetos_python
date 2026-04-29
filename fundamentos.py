NOMBRE = "luis"
print(" mi nombre es " + NOMBRE)

#tipo de escritura de variables


snake_case = "sena"
print(snake_case)

#Cuidaddo con las mayusculas y minusculas en las variables, ya que python es case sensitive
X = "esta una X en mayuscula"
print(X)

#TIPOS DE DATOS EN PYTHON
nombre = "luis"
apellido = "SILVA"
edad = 21
altura = 1.80
activo = True
correo = "senaluissilva883@gmail.com"
telefono = "3502222057"
cedula = 1234567890

# conversion de tipos de datos
telefono_int = int(telefono) #3502222057
edad_float = float(edad) #21.0
altura_int = int(altura) #1
cedula_str = str(cedula) #"1234567890"

#impresion de tipos de datos
print (type(nombre), nombre)
print (type(apellido), apellido)
print (type(edad), edad)
print (type(altura), altura)
print (type(activo), activo)
print (type(correo), correo)
print (type(telefono), telefono)
print (type(cedula), cedula)

# conversion de tipos de datos
print (type(telefono_int), telefono_int)
print (type(edad_float), edad_float)
print (type(altura_int), altura_int)
print (type(cedula_str), cedula_str)

"""Comentarios de bloque"""

#identacion en python
if 5 > 2:
    print ("5 es mayor que 2")
else :
    print ("5 no es mayor que 2")



#inputs en python
nombre_usuario = input("Ingrese su nombre: ")
print("Hola " + nombre_usuario + ", bienvenido a python")

edad_usuario = int(input("Ingrese su edad: "))
print("Tu edad es :", edad_usuario, "años")

# imprimir con formato f-string "f" es para combinar
print(f"hola {nombre_usuario}, tienes {edad_usuario} años")



