numeros_enteros = []

while len(numeros_enteros) != 8:
    numero = input("Ingrese un número entero: ").strip()

    if not numero.isdigit(): 
        print("El ingreso debe ser un número entero.")
        continue

    numeros_enteros.append(int(numero))

lista_ordenada = sorted(numeros_enteros)

numeros_enteros.reverse()

print(f"La lista ordenada: {lista_ordenada}")
print(f"La lista en reversa: {numeros_enteros}")

