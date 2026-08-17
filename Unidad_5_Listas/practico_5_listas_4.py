### EJERCICIO 4 ###

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []
#Recorro la lista y añado el dato si no se encuentra ya en la lista de datos_sin_repetidos
for dato in datos:
    if dato not in datos_sin_repetidos:
        datos_sin_repetidos.append(dato)
#Mostramos el resultado de la lista sin repetidos
print(f"La lista de datos sin valores repetidos: {datos_sin_repetidos}")