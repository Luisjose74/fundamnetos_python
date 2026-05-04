#operadores de asignación 

x = 5 
x = x + 3 # x ahora es igual a 8
x += 2 # x ahora es igual a 10
print(x)
x += 3 # x ahora es igual a 13
print(x)

x = x - 4 # x ahora es igual a 9
x -= 2 # x ahora es igual a 7
print(x)    

x = x * 2 # x ahora es igual a 14
x *= 3 # x ahora es igual a 42  
print(x)        

x = x / 2 # x ahora es igual a 21.0
x /= 3 # x ahora es igual a 7.0
print(x)

x = x % 3 # x ahora es igual a 1.0
x %= 2 # x ahora es igual a 1.0 
print(x)    

x = x ** 2 # x ahora es igual a 1.0
x **= 2 # x ahora es igual a 1.0
print(x)    

#walrus operator (operador de morsa)
print(x := 100) # Asigna 100 a x y luego imprime el valor de x


