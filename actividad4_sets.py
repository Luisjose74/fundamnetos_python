"""🎯 Actividad : Análisis de Matrículas del Centro de Formación
1. Crea actividad4_sets.py. Define los siguientes conjuntos de aprendices
matriculados por programa: 
python_curso = {'Ana','Luis','Marta','Carlos','Sofia','Pedro'} y 
java_curso = {'Luis','Carlos','Pedro','Laura','Diego'} y 
bd_curso = {'Marta','Sofia','Laura','Ana','Miguel'}.
2. Calcula e imprime usando operaciones de conjuntos: el total de aprendices únicos
en los tres programas (unión triple), los aprendices que cursan Python Y Java
simultáneamente, los aprendices que solo están en Python (no en Java ni en BD), y
los aprendices que están en exactamente dos programas (ni en uno solo ni en los
tres).
3. A partir de la siguiente lista con duplicados — inscripciones =
['Ana','Luis','Ana','Marta','Carlos','Luis','Sofia','Pedro','Ana'] — usa un conjunto para
determinar cuántos aprendices únicos se inscribieron y quiénes son.
4. Crea un diccionario conteo_programas donde cada clave sea el nombre de un
aprendiz (de la unión) y el valor sea el número de programas en los que está
matriculado. Usa comprensión de diccionario.
5. Bonus: Identifica e imprime quién está matriculado en los tres programas a la vez."""


python_curso = {'Ana','Luis','Marta','Carlos','Sofia','Pedro'} 
java_curso = {'Luis','Carlos','Pedro','Laura','Diego'} 
bd_curso = {'Marta','Sofia','Laura','Ana','Miguel'}

print(python_curso | java_curso | bd_curso) 
print(python_curso & java_curso) 
print(python_curso - java_curso) 
print(python_curso ^ java_curso) 

inscripciones = ['Ana','Luis','Ana','Marta','Carlos','Luis','Sofia','Pedro','Ana']
print(set(inscripciones))
print(len(set(inscripciones)))

conteo_programas = {nombre: 0 for nombre in python_curso | java_curso | bd_curso}
for nombre in inscripciones:
    conteo_programas[nombre] += 1
print(conteo_programas) 