# Actividad 3: Clasificador de IMC

# Función para ingresar peso y estatura con validación
def ingresar_peso():
    while True:
        try:
            peso = float(input("Ingrese su peso en kg: "))
            if peso > 0:
                return peso
            print("Error: El peso debe ser un valor positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            
# Función para ingresar estatura con validación
def ingresar_estatura():
    while True:
        try:
            estatura = float(input("Ingrese su estatura en metros: "))
            if estatura > 0:
                return estatura
            print("Error: La estatura debe ser un valor positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

# Solicitar peso y estatura
peso = ingresar_peso()
estatura = ingresar_estatura()

# Calcular IMC
imc = peso / (estatura ** 2)
# Clasificar IMC
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
    
# Imprimir resultado
print(f"Su IMC es: {imc:.2f} - Clasificación: {clasificacion}")
