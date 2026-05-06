#operadores aritméticos
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tipo_operacion = input("Ingrese el tipo de operación (suma, resta, multiplicacion, division, division_entera, modulo, potencia): ")

resultado = 0

if tipo_operacion == "suma":
    resultado = a + b
elif tipo_operacion == "resta":
    resultado = a - b
elif tipo_operacion == "multiplicacion":
    resultado = a * b
elif tipo_operacion == "division":
    if b == 0:
        print("Error: No se puede dividir por cero")
    else: 
        resultado = a / b
elif tipo_operacion == "division_entera":
    resultado = a // b
elif tipo_operacion == "modulo":
    resultado = a % b
elif tipo_operacion == "potencia":
    resultado = a ** b
else:
    print("Operación no reconocida")

print(f"Resultado: {resultado}")


