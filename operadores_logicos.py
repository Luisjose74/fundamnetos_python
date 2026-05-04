#operadores logicos

#and
print(True and True) #si ambos son verdaderos, devuelve True
print(True and False) #si alguno es falso, devuelve False
print(False and True) #si alguno es falso, devuelve False
print(False and False) #si ambos son falsos, devuelve False

#or
print(True or True) #si alguno es verdadero, devuelve True
print(True or False) #si alguno es verdadero, devuelve True
print(False or True) #si alguno es verdadero, devuelve True
print(False or False) #si ambos son falsos, devuelve False

#not
print(not True) #devuelve False
print(not False) #devuelve True

#EJERCICIO AND
print(5 > 3 and 2 < 4) #True and True -> True
print(5 > 3 and 5 < 4) #True and False -> False
print(2 > 3 and 2 < 4) #False and True -> False
print(2 > 3 and 5 < 4) #False and False -> False

#EJERCICIO OR
print(5 > 3 or 2 < 4) #True or True -> True
print(5 > 3 or 5 < 4) #True or False -> True
print(2 > 3 or 2 < 4) #False or True -> True
print(2 > 3 or 5 < 4) #False or False -> False

#EJERCICIO NOT
print(not (5 > 3)) #devuelve False
print(not (2 < 4)) #devuelve False
