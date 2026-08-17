### EJERCICIO 13 ###

#Lista de puntajes
puntajes = [450, 1200, 875, 990, 300, 1500, 640]

#Función Bubble_sort vista en clase
def bubble_sot_mejorado(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n-1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1 ], lista[j]
                intercambio = True
        if not intercambio:
            break
#Variables auxiliares para los puntajes mas altos y bajos
mas_alto = 0
mas_bajo = float('inf')

#Recorrido de la lista buscando los valores más altos y bajos
for puntos in puntajes:
    if puntos > mas_alto: mas_alto = puntos
    if puntos < mas_bajo: mas_bajo = puntos

#Llamado a la función para ordenar la lista
bubble_sot_mejorado(puntajes)

#Mostramos los datos que pide la consigna.
print("RANKING de PUNTAJES:")
for i in range(len(puntajes)):  
    if puntajes[i] == 990: 
        print(f"Posición {i + 1}: {puntajes[i]}  <---- Está es la posición buscada")
    else:
        print(f"Posición {i + 1}: {puntajes[i]}")
print(f"El puntaje más bajo es: {mas_bajo}")
print(f"El puntaje más alto es: {mas_alto}")


