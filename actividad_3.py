"""🎯 Actividad 3: Clasificador de IMC
1. Crea actividad3.py. Solicita al usuario su peso en kg y su estatura en metros.
2. Calcula el Índice de Masa Corporal con la fórmula:
IMC = peso / (estatura ** 2).
3. Usa if / elif / else para clasificar el resultado:
• Bajo peso (< 18.5),
• Normal (18.5–24.9),
• Sobrepeso (25–29.9),
• Obesidad (>= 30).
4. Imprime el valor del IMC y su clasificación correspondiente.
5. Bonus: Valida que el peso y la estatura sean valores positivos antes de calcular."""

# Actividad 3: Clasificador de IMC
def ingresar_peso():
    while True:
        try:
            peso = float(input("Ingrese su peso en kg: "))
            if peso > 0:
                return peso
            print("Error: El peso debe ser un valor positivo.")
        except ValueError:
            print("Error: Ingrese un número válido.")
            

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
