### EJERCICIO 8 ###

notas_alumnos = [
    [8,7,9],
    [4,10,8],
    [8,5,6],
    [7,7,9],
    [3,2,4]
]

promedios_alumnos = []
suma_materias = [0] * len(notas_alumnos[0])     #En esta parte tuve que investigar porque me daba error de indice por tener la lista vacia

for nota in notas_alumnos:
    #suma = nota[0] + nota[1] + nota[2] Este fue mi primer aprouch, pero luego investigando llegue a usar sum() y len()
    promedio = sum(nota) / len(nota)   #Asi ya no dependo de agregar las notas "a mano" si luego se agregan más
    promedios_alumnos.append(promedio)   #Se añade el promedio a la lista de promedios
    #Recorre las materias
    for materia in range(len(nota)):
        suma_materias[materia] += nota[materia] #Vamos adicionando cada materia en la posicion de la lista de sumas


#Se presenta la informacion de cada alumno y materia
print(f"El promedio de los alumnos fue: ")
for promedio in range(len(promedios_alumnos)):
    print(f"-Alumno {promedio + 1} fue: {promedios_alumnos[promedio]:.2f}")
print("El promedio por materias fue: ")
for materia in range(len(suma_materias)):
    print(f"-Materia {materia+1}: {suma_materias[materia] / len(notas_alumnos):.2f}")




