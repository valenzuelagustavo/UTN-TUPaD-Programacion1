### EJERCICIO N° 1 ###

#Lista de notas y variables para acumular y guardar más alta y baja
notas_alumnos = [10, 4, 5, 8, 9, 9, 7, 8, 6, 4]
nota_mas_baja = 10
nota_mas_alta = 0

notas_sumadas = 0
#Se recorre la lista y se acumulan las notas, adicionalmente se comparan más altas y más bajas
for nota in range(len(notas_alumnos)):
    notas_sumadas += notas_alumnos[nota]
    if notas_alumnos[nota] < nota_mas_baja: nota_mas_baja = notas_alumnos[nota]
    if notas_alumnos[nota] > nota_mas_alta: nota_mas_alta = notas_alumnos[nota]
#Se imprime el resultado
print(f"El promedio de notas de los alumnos es: {notas_sumadas / len(notas_alumnos):0.2f}. La nota más alta fue {nota_mas_alta:0.2f} y la más baja fue {nota_mas_baja:0.2f}.")