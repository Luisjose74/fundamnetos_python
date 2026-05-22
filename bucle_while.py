#buble while = es una estructura de control que se repite mientras una condicion sea verdadera true 

i = 0 # INICIALIZACION DEL BUCLE

while i < 6:
    print("Hola Mundo") # INSTRUCCION A REPETIR
    if i == 3: # CONDICION PARA SALIR DEL BUCLE
        break # SALE DEL BUCLE
    i += 1 # INCREMENTO DEL BUCLE
    
    
while i < 6:
    i += 1 # INCREMENTO DEL BUCLE
    if i == 3: # CONDICION PARA SALTAR LA ITERACION ACTUAL
        continue # SALTA LA ITERACION ACTUAL Y CONTINUA CON LA SIGUIENTE
    print(i)
else: # SE EJECUTA CUANDO LA CONDICION DEL BUCLE ES FALSA
    print("El bucle ha terminado")
    

#juego de pokemon 

puntos_de_vida = 100
pokemon = input("¿Que pokemon quieres usar? ")
# el bucle se repetira mientras los puntos de vida sean mayores a 0

while puntos_de_vida > 0:
    print(f"Tu pokemon {pokemon} tiene {puntos_de_vida} puntos de vida")
    ataque = input("¿Que ataque quieres usar? ")
    puntos_de_vida -= ataque # se resta el ataque a los puntos de vida
print(f"Tu pokemon {pokemon} ha sido derrotado")
