# Ejercicio creativo: Calculadora de SOAT para motos

""" 
- El costo del soat de una moto depende del cilindraje de la moto, el cual 
se clasifica en las siguientes categorías.
- Año de fabricación.
- El costo del soat también se ve afectado por el año de fabricación de la moto,
con un descuento del 10% para motos fabricadas hace menos de 5 años.
- El programa debe solicitar al usuario el cilindraje y el año de fabricación de la moto, 
y luego calcular y mostrar el costo del soat correspondiente.
- Calculadora de SOAT para motos
- Tarifas reales 2026."""

print("Calculadora de SOAT para motos")
print("Ingrese los datos de la moto para calcular el costo del SOAT")
print("=" * 50)

# 1. Solicitar al usuario el cilindraje y el año de fabricación de la moto
marca_moto = input("Ingrese la marca de la moto: ")

# 2. Solicitar al usuario el cilindraje de la moto
print("""
Seleccione la clase de vehículo:
1. Ciclomotor                          → $124,100
2. Menos de 100 c.c.                   → $256,200
3. De 100 a 200 c.c.                   → $343,300
4. Más de 200 c.c.                     → $761,400
5. Motocarro, tricimoto, cuadriciclo   → $386,900
6. Motocarro 5 pasajeros               → $386,900
""")    

# 3. Validar la opción ingresada por el usuario
opcion = int(input("Ingrese el número de su opción: "))

# 4. Solicitar al usuario el año de fabricación de la moto
anio_fabricacion = int(input("Ingrese el año de fabricación de la moto: "))

print("=" * 50)

# 5. Asignar tarifa según clase de vehículo
tarifas = {
    1: (124_100, "Ciclomotor"),
    2: (256_200, "Menos de 100 c.c."),
    3: (343_300, "De 100 a 200 c.c."),
    4: (761_400, "Más de 200 c.c."),
    5: (386_900, "Motocarro, tricimoto, cuadriciclo"),
    6: (386_900, "Motocarro 5 pasajeros"),
}
# Validar opción ingresada
if opcion not in tarifas:
    print("❌ Opción no válida.")
else:
    costo_soat, clase = tarifas[opcion]

    # 6. Aplicar descuento si la moto es nueva ✅
    anio_actual = 2026
    antiguedad = anio_actual - anio_fabricacion

# Aplicar descuento del 10% para motos con antigüedad de 5 años o menos
    if antiguedad <= 5:   # ✅ Corregido
        costo_soat = costo_soat * (1 - 0.10)
        print(f"✅ Descuento del 10% aplicado ({antiguedad} años recientes)")
    else:
        print(f"ℹ️  Sin descuento ({antiguedad} años de antigüedad)")



    # 7. Resultado final
    print(f"""
{'=' * 50}
🏍️   Marca         : {marca_moto}
📋  Clase         : {clase}
📅  Año           : {anio_fabricacion} ({antiguedad} años)
💰  Total a pagar : ${costo_soat}
{'=' * 50}
""")
    
    