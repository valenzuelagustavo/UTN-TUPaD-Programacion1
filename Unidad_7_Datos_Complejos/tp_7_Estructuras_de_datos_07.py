### Ejercicio 7 ###

asistencias = ["Ana","Luis","Ana","María", "Luis", "Pedro", "Ana"]

asistencia_set = set(asistencias)

repeticiones = {}

print("Lista de asistencia completa\n---------------------------")
for n in range(len(asistencias)):
    print(f"\t{asistencias[n]}")

print(f"\nAlumnos que asistieron: ")
print(*asistencia_set)

print("\nCantidad de veces que \nasistio cada alumno: ")
for i, alumno in enumerate(asistencias):
    repeticiones[alumno] = repeticiones.get(alumno, 0) + 1
for alumno, cantidad in repeticiones.items():
    print(f"\t{alumno}: {cantidad}")