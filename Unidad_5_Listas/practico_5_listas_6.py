### Ejercicio 6 ###

lista_numeros = [4,5,8,10,7,3,2]
lista_auxiliar = []
#Recorro la lista y asigno los valores a la lista auxiliar (empzando en -1 para que el ultimo quede primero)
for i in range(-1,7): lista_auxiliar.append(lista_numeros[i])
for i in range(7): lista_numeros[i] = lista_auxiliar[i]   #Reasigno los números de lista auxiliar a lista_numeros con su nuevo orden 
#Muestro la lista_numeros reordenada
print(f"La lista reordenada: {lista_numeros}")