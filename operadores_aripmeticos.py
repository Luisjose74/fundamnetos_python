#operadores aritméticos

a = 10
b = 5

#suma
suma = a + b
print(f"La suma de {a} y {b} es: {suma}")


#resta
resta = a - b
print(f"La resta de {a} y {b} es: {resta}")


#multiplicación
multiplicacion = a * b
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")


#división
division = a / b
print(f"La división de {a} y {b} es: {division}")


#división entera
division_entera = a // b
print(f"La división entera de {a} y {b} es: {division_entera}")


#módulo
modulo = a % b
print(f"El módulo de {a} y {b} es: {modulo}")


#potencia
potencia = a ** b
print(f"La potencia de {a} elevado a {b} es: {potencia}")

#precedencia de operadores
resultado = a + b * 2
print(f"El resultado de la expresión a + b * 2 es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la expresión (a + b) * 2 es: {resultado_2}")

resultado_3 = a ** b * 2
print(f"El resultado de la expresión a ** b * 2 es: {resultado_3}")

resultado_4 = (a ** b) * 2
print(f"El resultado de la expresión (a ** b) * 2 es: {resultado_4}")

resultado_5 = a ** (b * 2)
print(f"El resultado de la expresión a ** (b * 2) es: {resultado_5}")



ejercicio_1 = ((a + b) * (a - b) / (a ** b)) - ((a * b) % (a + b))

print(f"El resultado del ejercicio 1 es: {ejercicio_1}")

#libreria matemática

import math
print(math.pi) 

#libreria random aletorio 
import random 
numero_aleatorio = random.randint(1, 100)
print(f"El número aleatorio generado es: {numero_aleatorio}")
