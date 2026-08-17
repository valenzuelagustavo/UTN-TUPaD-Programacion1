### EJERCIO 3 ###

#Importo random para el manejo de los números aleatorios
import random as rm
#Listas
num_pares = []
num_impares = []
lista_numeros = []
#Añado los números aleatorios a la lista
for numeros in range(15):
    lista_numeros.append(rm.randint(1, 100))
#Muestro la lista, no lo pide la consigna pero para controlar el resultado
print(f"La lista de números aleatorios es: {lista_numeros}")
#Recorro la lista y añado a las listad de impares o pares según corresponda
for i in range(len(lista_numeros)):
    if lista_numeros[i] % 2 == 0: num_pares.append(i)   #Añadimos los pares
    elif lista_numeros[i] % 2 != 0: num_impares.append(i)    #Añadimos los impares
#Informo la cantidad de pares e impares
print(f"La lista de números impares tiene {len(num_impares)} números. La lista de números pares tiene {len(num_pares)} números.")

