### EJERCICIO 12 ###

#Lista de numeros enteros
numeros_enteros = []

#Búcle de carga de la lista (hasta que su tamaño sea de 8 entradas)
while len(numeros_enteros) != 8:
    numero = input("Ingrese un número entero: ").strip()
    #Si no es un digito damos mensaje al usuario y volvemos al comienzo del búcle
    if not numero.isdigit(): 
        print("El ingreso debe ser un número entero.")
        continue
    #Añadimos el número a la lista de número entero
    numeros_enteros.append(int(numero))
#Asignamos la lista ordenada 
lista_ordenada = sorted(numeros_enteros)
#Hacemos que la lista se ponga en reversa
lista_en_reversa = sorted(numeros_enteros, reverse=True)

#Imprimimos los resultados
print(f"La lista ordenada: {lista_ordenada}")
print(f"La lista en reversa: {lista_en_reversa}")

