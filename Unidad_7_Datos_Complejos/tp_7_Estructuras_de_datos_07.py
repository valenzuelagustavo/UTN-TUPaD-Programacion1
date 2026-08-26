### Ejercicio 7 ###
"""Script de análisis de asistencias que procesa un registro diario para obtener la lista de empleados presentes y la cantidad de jornadas a las que asistió cada uno."""

asistencias = ["Ana","Luis","Ana","María", "Luis", "Pedro", "Ana"]

asistencia_set = set(asistencias)

repeticiones = {}

print("Lista de asistencia completa\n---------------------------")
for alumno in asistencias:
    print(f"\t{alumno}")

print(f"\nAlumnos que asistieron: ")
print(*asistencia_set)

print("\nCantidad de veces que \nasistio cada alumno: ")
for alumno in asistencias:
    repeticiones[alumno] = repeticiones.get(alumno, 0) + 1
for alumno, cantidad in repeticiones.items():
    print(f"\t{alumno}: {cantidad}")