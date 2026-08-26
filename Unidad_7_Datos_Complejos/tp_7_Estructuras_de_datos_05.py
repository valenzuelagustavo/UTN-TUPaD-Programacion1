### Ejercicio 5 ###

frase_usuario = input("Ingrese una frase para analizarla: ").lower().split()

palabras_unicas = set(frase_usuario)

cuenta_palabras = {}

#for i, palabra in enumerate(frase_usuario, start=1):
#    cuenta_palabras[palabra] = cuenta_palabras.get(palabra, 0) + 1

for palabra in frase_usuario:
    cuenta_palabras[palabra] = cuenta_palabras.get(palabra, 0) + 1

print(f"Las palabras únicas: {palabras_unicas}")
print(f"Recuento de palabras: {cuenta_palabras}")