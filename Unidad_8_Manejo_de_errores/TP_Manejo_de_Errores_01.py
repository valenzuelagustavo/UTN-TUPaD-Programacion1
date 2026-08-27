"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 1
Identifica y documenta mediante comentarios los errores de ejecución (TypeError e IndexError) 
presentes en el código proporcionado.
"""
a = 10 
b = input("Introduce un número: ") 
result = a / b    #Error: TypeError. 'b' es un string asi que no permite la división
print(f"Resultado: {result}") 


numbers = [1, 2, 3] 
print(numbers[5])  #Error: IndexError. [5] esta fuera del rango de la lista numbers.