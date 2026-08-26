### Ejercicio 10 ###
"""Script que procesa un diccionario de países y capitales para generar un nuevo diccionario invertido, utilizando las capitales como claves."""

original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Paraguay": "Asunción", "Uruguay": "Montevideo"}
invertido = {}

for pais, capital in original.items():
    invertido.update({capital: pais})

print(original)
print(invertido)