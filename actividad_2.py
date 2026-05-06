# Actividad 2: Calificaciones Parciales

# paso 1: solicitar las calificaciones parciales
# paso 2: calcular el promedio de las calificaciones
# paso 3: imprimir el promedio y el estado de aprobado o no aprobado (aprobado si el promedio es mayor o igual a 3.0)
# Bonus: Validar que las calificaciones sean números entre 0 y 5 antes de calcular el promedio.

print("=" * 70)
def ingresar_nota(numero):                  # Función para ingresar una calificación parcial
    while True:
        try:                                # Validar que la calificación sea un número entre 0 y 5
            nota = float(input(f"Ingrese la calificación parcial {numero}: "))
            if 0 <= nota <= 5.0:
                return nota
            print("Error: La calificación debe estar entre 0 y 5.0")
        except ValueError:                  # Validar que la calificación sea un número
            print("Error: Ingrese un número válido.")
            
print("Bienvenido A La Actividad 2")

print("-" * 70)

notas = [ingresar_nota(i) for i in range(1, 4)]           # Solicitar las calificaciones parciales
promedio = sum(notas) / len(notas)                        # Calcular el promedio de las calificaciones
puntos_faltantes = 5.0 - promedio
aprobado = promedio >= 3.0

print("-" * 70)

print(f"Promedio:         {promedio:.2f}")                # Imprimir el promedio con dos decimales
print(f"Puntos faltantes: {puntos_faltantes:.2f}")

print("-" * 70)

print(f"Estado:           {'👍 Aprobado' if aprobado else '❌ No aprobado'}")

print("=" * 70)
