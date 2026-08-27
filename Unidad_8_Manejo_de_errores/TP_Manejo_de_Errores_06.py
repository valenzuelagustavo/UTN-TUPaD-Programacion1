"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 6
Solicita un número al usuario y valida la entrada mediante try-except, capturando errores 
de valor si se ingresa texto y cualquier otra excepción inesperada.
"""
try:
    numero_usuario = float(input("Ingrese un número: "))
    print(f"El número ingresado es {numero_usuario}")
except ValueError:
    print("Debe ingresar un número valido.")
except Exception as e:
    print(f"Se produjo un error inesperado. Error: {e}")