# Actividad 2: Listas y Slicing
""" 1. Crea actividad2_listas.py con la siguiente lista de temperaturas registradas durante
dos semanas (14 días): temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18,
20, 22, 19].
2. Usa indexación para imprimir la temperatura del primer día, el último día, el día 7
(mitad) y el penúltimo día, usando tanto índices positivos como negativos.
3. Usa slicing para extraer e imprimir: la primera semana (días 1–7), la segunda
semana (días 8–14), solo los días pares de toda la quincena y la lista de
temperaturas en orden invertido.
4. Calcula e imprime la temperatura promedio de cada semana por separado usando
sum() y len() aplicados a los slices.
5. Bonus: Determina cuál de las dos semanas tuvo mayor temperatura promedio y
muestra el resultado con un mensaje descriptivo. """


temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

print("Temperatura del primer día:", temperaturas[0])
print("Temperatura del último día:", temperaturas[-1])
print("Temperatura del día 7 (mitad):", temperaturas[6])
print("Temperatura del penúltimo día:", temperaturas[-2])

print("Primera semana:", temperaturas[0:7])
print("Segunda semana:", temperaturas[7:14])
print("Días pares:", temperaturas[0:14:2])
print("Temperaturas en orden inverso:", temperaturas[::-1]) 

primera_semana = temperaturas[0:7]
segunda_semana = temperaturas[7:14]

promedio_primera_semana = sum (primera_semana) / len(primera_semana)
promedio_segunda_semana = sum (segunda_semana) / len(segunda_semana)

print(f"Temperatura promedio de la primera semana: {promedio_primera_semana:.2f}")
print(f"Temperatura promedio de la segunda semana: {promedio_segunda_semana:.2f}")

if promedio_primera_semana > promedio_segunda_semana:
    print("La primera semana tuvo una temperatura promedio mayor.")
else:    
      print("La segunda semana tuvo una temperatura promedio mayor.")