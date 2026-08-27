"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 7
Implementa un bucle while junto con bloques try-except para solicitar un número cíclicamente,
permitiendo al usuario volver a intentar si ingresa un valor inválido.
"""

while True:
    try:
        numero_usuario = float(input("Ingrese un número: "))
        print(f"El número ingresado es {numero_usuario}")
        break
    except ValueError:
        print("Debe ingresar un número valido.")
    except Exception as e:
        print(f"Se produjo un error inesperado. Error: {e}")