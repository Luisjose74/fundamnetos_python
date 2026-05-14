#ACTIVIDAD 1: INVENTARIO DE LA TIENDA ESCOLAR

"""1. Crea actividad1_listas.py. Declara una lista llamada productos con al menos 6
artículos de una tienda escolar (cuadernos, lapiceros, etc.), usando strings.
2. Declara una segunda lista precios con los precios correspondientes a cada producto
(usa floats). Asegúrate de que ambas listas tengan el mismo número de elementos.
3. Declara una tercera lista cantidades con la cantidad disponible de cada artículo
(enteros).
4. Imprime las tres listas completas y luego usa len() para mostrar cuántos productos
tiene el inventario.
5. Muestra el tipo de dato de la lista usando type() y el tipo del primer elemento
usando type(productos[0]). Explica la diferencia en los comentarios de tu código."""

productos = ["Cuaderno", "Lapicero", "Borrador", "Regla", "Mochila", "Calculadora"]
precios = [2.50, 0.75, 0.50, 1.00, 25.00, 15.00]
cantidades = [100, 200, 150, 80, 50, 30]
cantidad_productos = len(productos)

print("inventario de la tienda escolar:"
      "\nProductos:", productos,
      "\nPrecios:", precios,
      "\nCantidades:", cantidades,
      "\nCantidad de productos:", cantidad_productos)

print(f"El producto '{productos[0]}' tiene un precio de {precios[0]} y hay {cantidades[0]} unidades disponibles.")

print(f"El producto '{productos[1]}' tiene un precio de {precios[1]} y hay {cantidades[1]} unidades disponibles.")

print(f"El producto '{productos[2]}' tiene un precio de {precios[2]} y hay {cantidades[2]} unidades disponibles.")

print(f"El producto '{productos[3]}' tiene un precio de {precios[3]} y hay {cantidades[3]} unidades disponibles.")

print(f"El producto '{productos[4]}' tiene un precio de {precios[4]} y hay {cantidades[4]} unidades disponibles.")

print(f"El producto '{productos[5]}' tiene un precio de {precios[5]} y hay {cantidades[5]} unidades disponibles.")

print(type(productos))
print(type(precios))
print(type(cantidades))
print(type(precios[0]))
print(type(precios[0]))
print(type(cantidades[0]))
