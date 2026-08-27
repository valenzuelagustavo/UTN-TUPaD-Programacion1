"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 2
Resuelve los errores del código original ajustando la conversión de tipos de datos y
los índices de la lista, sin utilizar manejo de excepciones.
"""
a = 10 
b = input("Introduce un número: ") 
result = a / float(b)    #Paso el input del usuario a float para que se pueda realizar la división
print(f"Resultado: {result}") 


numbers = [1, 2, 3] 
print(numbers[2])   #Ajusto el indice en el print. También se podria agregar más items a la lista. 