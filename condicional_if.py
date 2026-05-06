#CONDIFIONAL IF / ELSE / ELIF

if True:
    print("Es verdadero")
elif False:
    print("Es verdadero")
elif True:
    print("Es verdadero")
else:
    print("Es falso") 

#EJERCICIO 1

edad = 17
if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("eres adulto") 
else:
    print("Eres mayor de edad")
    

Edad = int(input("Ingrese su edad: "))

if Edad < 18:
    if Edad > 12 and Edad < 18:
        print("Eres un adolescente")
    else:        
        print("Eres un niño")
else:
    if Edad >= 18 and Edad < 65:
        print("Eres un adulto")
    else:
        print("Eres mayor de edad")

#EJERCICIO 2

numero = 4
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("el numero es par" if numero % 2 == 0 else "El numero es impar")

