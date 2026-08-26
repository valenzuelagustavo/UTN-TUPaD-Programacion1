### Ejercicio 6 ###

alumnos = {}
notas = []

for i in range(3):
    notas.clear()
    alumno = input("Ingrese el nombre del alumno: ")

    for nota in range(3):
        notas.append(input("Ingrese la nota: "))

    alumnos.update({alumno: tuple(notas)})


print(alumnos)