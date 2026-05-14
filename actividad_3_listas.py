"""🎯 Actividad 3: Gestión de Lista de Reproducción Musical
1. Crea actividad3_listas.py. Declara una lista canciones con 5 nombres de canciones
de tu género favorito.
2. Aplica los siguientes métodos en orden y muestra el estado de la lista después de
cada uno: append() para agregar una canción nueva al final; insert() para agregar
otra canción en la segunda posición; extend() para fusionar con esta lista: ["Bonus
Track 1", "Bonus Track 2"].
3. Usa remove() para eliminar una canción por su nombre y pop() para eliminar la
última canción, guardando el valor eliminado e imprimiéndolo.
4. Usa sort() para ordenar la lista alfabéticamente y muéstrala ordenada.
5. Responde estas preguntas usando métodos: ¿Cuántas canciones tiene la playlist?
¿En qué posición está la primera canción que agregaste? ¿Cuántas veces aparece
el string 'Bonus Track 1'?"""

print("Gestión de Lista de Reproducción Musical")

canciones = ["detras de tu arma", "los hombres no deben llorar", "el mejor - remix",
"immortals", "frecuencia" ]

print("Lista de canciones inicial:", canciones)

canciones.append("algo me gusta de ti")
print("Lista de canciones con una nueva cancion:", canciones)

canciones.insert(2, "Primer Amor")
print("Lista de canciones con una nueva cancion:", canciones)

canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print("Lista de canciones con nuevas canciones:", canciones)

cancion_eliminada = canciones.pop()
print("Canción eliminada:", cancion_eliminada)
print("Lista de canciones sin la ultima cancion:", canciones)

cancion_eliminada = canciones.remove("Primer Amor")
print("Canción eliminada:", cancion_eliminada)
print("Lista de canciones sin la cancion 'Primer Amor':", canciones)

canciones.sort()
print("Lista de canciones ordenada:", canciones)

cantidad_canciones = len(canciones)
print("Cantidad de canciones:", cantidad_canciones)

posicion_primera_cancion = canciones.index("los hombres no deben llorar")
print("Posicion de la primera cancion:", posicion_primera_cancion)

cantidad_bonustack = canciones.count("Bonus Track 1")
print("Cantidad de Bonus Track 1:", cantidad_bonustack)



