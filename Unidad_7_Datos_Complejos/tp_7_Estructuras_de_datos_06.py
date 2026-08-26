### Ejercicio 6 ###
"""Programa que registra a un grupo de alumnos junto con sus notas y calcula el promedio general de cada estudiante."""

alumnos = {}

for i in range(3):
    notas = []
    alumno = input("Ingrese el nombre del alumno: ")
    for nota in range(3): 
        notas.append(int(input("Ingrese la nota: ")))
    alumnos.update({alumno: tuple(notas)})

for alumno, nota in alumnos.items():
    promedio = sum(nota) / len(nota)
    print(f"Alumno {alumno}\nNotas: {nota}\nPromedio: {promedio:.2f}\n\n")


