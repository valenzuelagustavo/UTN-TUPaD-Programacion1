### Ejercicio 1 ###

precios_frutas = {
    'Banana': 1200,
    'Anana': 2500, 
    'Melón': 3000, 
    'Uva': 1450
    }

#Se añaden nuevos pares clave/valor al diccionario
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})


#Se hace un update del precio
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})


frutas = list(precios_frutas.keys())

print(frutas)
