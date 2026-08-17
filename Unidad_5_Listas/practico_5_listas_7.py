### EJERCICIO 7 ###
#Matriz de temperaturas
lista_temperaturas = [
    [12,28],
    [7,21],
    [10,25],
    [10,26],
    [14,31],
    [15,30],
    [13,26]
]
#Variables auxiliares
promedio_min = 0
promedio_max = 0
dia_rango = 0
dia = 0
#Recorro la lista de temperaturas 
for fila in lista_temperaturas:
    promedio_min += fila[0]     #Se suman las temperaturas minimas
    promedio_max += fila[1]     #Se suman las temperaturas maximas

    amplitud = fila[1] - fila[0]    #Se calcula el rango de temperaturas
    #Si el rango es mayor pasa a ser el nuevo rango maximo
    if amplitud > dia_rango: 
        dia_rango = amplitud
        amplitud_dia = fila

#Se muestran los resultados por consola
print(f"El promedio minimo de temperatura fue de {promedio_min / len(lista_temperaturas):.2f}° y el promedio maximo fue de {promedio_max / len(lista_temperaturas):.2f}°")
print(f"La mayor amplitud termica fue de {dia_rango}°, el día en que la temperatura fue entre {amplitud_dia[0]}° y {amplitud_dia[1]}°")