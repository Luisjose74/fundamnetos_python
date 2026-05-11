#Ejercicio 1 

"""crear las siguientes variables según su criterio:

• Una variable que permita almacenar el nombre de una persona.
• Una variable que permita almacenar un valor de un producto.
• Una variable que permita almacenar el promedio de una asignatura.
• Imprima en consola las variables creadas"""

nombre_persona = "Juan"
valor_producto = 100.50
promedio_asignatura = 85.75

print("El nombre de la persona es:", nombre_persona)
print("El valor del producto es:", valor_producto)
print("El promedio de la asignatura es:", promedio_asignatura)  

#Ejercicio 2

"""Crear programa que lea tipos de datos y los relacione con operadores
introducidos por teclado : dos enteros, un float, dos String.

• Se deben sumar los tres número y se muestran en pantalla.
• Se debe visualizar el entero mayor.
• Se debe visualizar el resultado de la división del float con el resto de
la división de los dos enteros.
• Se debe visualizar la concatenación de las dos cadenas leídas."""

valor_entero1 = int(input("Ingrese el primer número entero: "))
valor_entero2 = int(input("Ingrese el segundo número entero: "))
valor_float = float(input("Ingrese un número decimal: "))

suma = valor_entero1 + valor_entero2 + valor_float
print(F"La suma de los tres números es: {suma}")

#ejercicio 3

"""Crear 2 variables enteras, una llamada “Base” y la otra “Exponente”,
asignar valores a su criterio. Calcular la potencia utilizando y mostrar el
resultado de la operación."""

base = 2
exponente = 3
potencia = base ** exponente
print(f"El resultado de {base} elevado a la {exponente} es: {potencia}")

#Ejercicio 4

"""Hallar la raíz cuadrada de los siguientes números 2, 8, 9, 27, 28, 55, 121
y mostrar los resultados de cada operación."""

numeros = [2, 8, 9, 27, 28, 55, 121]
for numero in numeros:
    raiz_cuadrada = numero ** 0.5
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
    
    
#Ejercicio 5

"""
• Crear una variable para almacenar el nombre de un estudiante.
• Crear 5 variables para almacenar 5 diferentes notas decimales.
• Calcular el promedio final del estudiante a partir de las 5 notas
decimales. (Recuerda que un promedio se calcula sumando todos los
valores y dividiendo el resultado por el número de valores).
• Mostrar el resultado y el nombre del estudiante.
"""
Nombre_estudiante = "Maria Gomez"
nota1 = 85.5
nota2 = 90.0
nota3 = 78.5
nota4 = 92.0
nota5 = 95.0

promedio_final = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f"El promedio final de {Nombre_estudiante} es: {promedio_final}")

#Ejercicio 6

"""Crear una variable entera de nombre “numeroUno” con el valor de 8 y
una variable entera de nombre “numeroDos” con el valor de 2.
Intercambiar los valores de ambas variables, de modo que
“numeroUno” valga 2, y

“numeroDos” valga 8. (Utiliza una variable

auxiliar). Mostrar los resultados de ambas variables."""

numeroUno = 8
numeroDos = 2

auxiliar = numeroUno
numeroUno = numeroDos
numeroDos = auxiliar

print(f"El valor de 'numeroUno' es: {numeroUno}")
print(f"El valor de 'numeroDos' es: {numeroDos}")

#Ejercicio 7

"""Crear una variable booleana llamada “Estado”. Realizar la siguiente
operación sobre la variable “Estado”: (5 == 2) || (2 > 1). Mostrar el
resultado de la variable “Estado”."""

Estado = (5 == 2) or (2 > 1)
print(f"El resultado de la variable 'Estado' es: {Estado}")


#Ejercicio 8

"""• Crear una variable llamada “Resultado”.
• Dentro de la variable “Resultado”, crear una operación aritmética
donde se haga uso de todos los operadores matemáticos en
repetidas ocasiones con los números que tú determines.
• Ejemplo: (9/2) +8*2/1-(2+2) ....
• Mostrar el resultado de la operación."""

Resultado = (9 / 2) + (8 * 2) / 1 - (2 + 2) + (5 ** 2) - (10 % 3)
print(f"El resultado de la operación es: {Resultado}")

#ejercicio 9

"""• Crear una variable entera llamada “ladoCuadrado” de valor 8 y calcular el área y el
perímetro del cuadrado a partir de la variable anteriormente creada.
• Crear una variable entera llamada “baseTriangulo” de valor 9 y una variable
entera llamada “alturaTriangulo” de valor 8. Crear dos variables enteras llamadas
“ladoUnoTriangulo” y

“ladoDosTriangulo” de valor 8 ambas. Calcular el área y el

perímetro del triángulo a partir de variables anteriormente creadas.
• Crear una variable entera llamada “baseRectangulo” de valor 8 y una variable
entera llamada “alturaRectangulo” de valor 6. Calcular el área y el perímetro del
rectángulo a partir de variables anteriormente creadas."""

ladoCuadrado = 8
area_cuadrado = ladoCuadrado ** 2
perimetro_cuadrado = ladoCuadrado * 4

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8
area_triangulo = (baseTriangulo * alturaTriangulo) / 2
perimetro_triangulo = ladoUnoTriangulo + ladoDosTriangulo + baseTriangulo

baseRectangulo = 8
alturaRectangulo = 6
area_rectangulo = baseRectangulo * alturaRectangulo
perimetro_rectangulo = 2 * (baseRectangulo + alturaRectangulo)

print(f"El área del cuadrado es: {area_cuadrado}")
print(f"El perímetro del cuadrado es: {perimetro_cuadrado}")
print(f"El área del triángulo es: {area_triangulo}")
print(f"El perímetro del triángulo es: {perimetro_triangulo}")
print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El perímetro del rectángulo es: {perimetro_rectangulo}")

#Ejercicio 10

"""• Desarrollar un programa que permita por medio de la edad de una persona,
determinar la categoría en la que pertenece a raíz de la siguiente tabla:

• Rango de edad Categoría
• 0 - 5 Infante
• 6 - 10 Niño
• 11 - 15 Pre adolescente
• 16 - 18 Adolescente
• 19 - 25 Pre adulto
• 26 - 40 Adulto
• 41 - 55 Pre anciano
• 56+ Anciano"""

edad = int(input("Ingrese su edad: "))

if 0 <= edad <= 5:
    categoria = "Infante"
elif 6 <= edad <= 10:
    categoria = "Niño"
elif 11 <= edad <= 15:
    categoria = "Pre adolescente"
elif 16 <= edad <= 18:
    categoria = "Adolescente"
elif 19 <= edad <= 25:
    categoria = "Pre adulto"
elif 26 <= edad <= 40:
    categoria = "Adulto"
elif 41 <= edad <= 55:
    categoria = "Pre anciano"
else:
    categoria = "Anciano"
    
print(f"Con una edad de {edad} años, perteneces a la categoría: {categoria}")
