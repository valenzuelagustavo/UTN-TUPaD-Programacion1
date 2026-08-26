original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Paraguay": "Asunción", "Uruguay": "Montevideo"}
invertido = {}

"""
Primera implementación
paises = []
capitales = []
for pais in original.keys(): paises.append(pais)
for capital in original.values(): capitales.append(capital)
"""
for pais, capital in original.items():
    invertido.update({capital: pais})

print(original)
print(invertido)