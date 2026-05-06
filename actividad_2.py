def ingresar_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación parcial {numero}: "))
            if 0 <= nota <= 5.0:
                return nota
            print("Error: La calificación debe estar entre 0 y 5.0")
        except ValueError:
            print("Error: Ingrese un número válido.")
            
print("Bienvenido A La Actividad 2")
print("=" * 70)

notas = [ingresar_nota(i) for i in range(1, 4)]
promedio = sum(notas) / len(notas)
puntos_faltantes = 5.0 - promedio
aprobado = promedio >= 3.0

print("=" * 70)

print(f"Promedio:         {promedio:.2f}")
print(f"Puntos faltantes: {puntos_faltantes:.2f}")
print(f"Estado:           {'✓ Aprobado' if aprobado else '✗ No aprobado'}")

print("=" * 70)
