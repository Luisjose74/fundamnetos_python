"""🎯 Actividad : Sistema de Registro de Aprendices
1. Crea actividad2_diccionarios.py. Construye un diccionario grupo donde cada clave
sea el número de ficha (int) y el valor sea otro diccionario con los campos: nombre,
edad, notas (lista de 4 floats) y ciudad. Registra al menos 4 aprendices.
2. Escribe una formula calcular_promedio que reciba la lista de notas y retorne el
promedio. Úsala al mostrar el reporte.
3. Usando .items() y un ciclo for, imprime un reporte con: ficha, nombre, edad,
promedio de notas y estado (APROBADO/REPROBADO según si el promedio >=
3.0).
4. Agrega un nuevo aprendiz al diccionario después de crearlo, usando una nueva
clave de ficha. Luego actualiza la ciudad de uno de los aprendices existentes con
dicc[ficha]['ciudad'] = 'Nueva Ciudad'.
5. Bonus: Usa sorted() con key= para imprimir la lista de aprendices ordenada de
mayor a menor promedio."""


grupo_adso = {
    1: {
        "nombre": "Juan",
        "edad": 20,
        "notas": [1.5, 3.0, 2.0, 1.5],
        "ciudad": "Ciudad A"
    },
    
    2: {
        "nombre": "Maria",
        "edad": 22,
        "notas": [9.0, 8.5, 7.5, 8.0],
        "ciudad": "Ciudad B"        
    },
    
    3: {
        "nombre": "Pedro",
        "edad": 19,
        "notas": [7.5, 8.0, 9.0, 7.5],
        "ciudad": "Ciudad C"
    },
    
    4: {
        "nombre": "Luis",
        "edad": 21,
        "notas": [8.0, 9.0, 7.5, 8.5],
        "ciudad": "Ciudad D"        
    }
}


def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio 

for ficha, aprendiz in grupo_adso.items():
    promedio = calcular_promedio(aprendiz["notas"])
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"
    print(f"Ficha: {ficha}")
    
    print(f"Nombre: {aprendiz['nombre']}")
    print(f"Edad: {aprendiz['edad']}")
    print(f"Promedio: {promedio}")
    print(f"Estado: {estado}")
    print("-" * 20)
    
    