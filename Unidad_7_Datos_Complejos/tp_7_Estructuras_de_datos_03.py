### Ejercicio 3 ###
"""Script que extrae los nombres de las frutas de un catálogo de precios y los almacena en una lista independiente."""

precios_frutas = {
    'Banana': 1200,
    'Anana': 2500, 
    'Melón': 3000, 
    'Uva': 1450
    }

precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})

frutas = list(precios_frutas.keys())

print(frutas)
