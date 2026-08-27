"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 3
Implementa bloques try-except básicos para capturar los errores del código original
y evitar que la ejecución del programa se interrumpa.
"""
a = 10 
b = input("Introduce un número: ") 
try:
    result = a / b   
    print(f"Resultado: {result}") 
except TypeError:
    print("Ingreso invalido. Debe ingresar un número.")


numbers = [1, 2, 3]
try: 
    print(numbers[5])  
except IndexError:
    print("Indice fuera de rango.")