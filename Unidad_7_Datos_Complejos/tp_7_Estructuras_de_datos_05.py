### Ejercicio 5 ###
"""Script que analiza una frase ingresada por el usuario para extraer su vocabulario único y calcular la frecuencia de aparición de cada palabra."""

frase_usuario = input("Ingrese una frase para analizarla: ").lower().split()

palabras_unicas = set(frase_usuario)

cuenta_palabras = {}

for palabra in frase_usuario:
    cuenta_palabras[palabra] = cuenta_palabras.get(palabra, 0) + 1

print(f"Las palabras únicas: {palabras_unicas}")
print(f"Recuento de palabras: {cuenta_palabras}")