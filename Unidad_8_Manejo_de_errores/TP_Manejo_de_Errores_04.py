"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 4
Utiliza excepciones múltiples para capturar, identificar y manejar de forma 
específica distintos tipos de errores (como TypeError, IndexError o ZeroDivisionError).
"""
a = 10 
b = input("Introduce un número: ") 
try:
    result = a / b   
    print(f"Resultado: {result}") 
except TypeError:
    print("Ingreso invalido. Debe ingresar un número.")
except ZeroDivisionError:
    print("Valor invalido. No se puede dividir por 0.")


numbers = [1, 2, 3]
try: 
    print(numbers[5])  
except IndexError:
    print("Indice fuera de rango.")
except TypeError:
    print("Tipo de dato invalido.")