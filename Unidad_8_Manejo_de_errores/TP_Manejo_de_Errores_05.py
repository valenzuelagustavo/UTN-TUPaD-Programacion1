"""
Trabajo Práctico 8: Manejo de errores - Ejercicio 5
Completa la estructura de manejo de errores agregando los bloques 'else' (ejecutado si no hay errores)
y 'finally' (ejecutado siempre al finalizar).
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
else:
    print("División realizada perfectamente.")
finally:
    print("El camino al infierno esta empedrado con buenas intenciones.")


numbers = [1, 2, 3]
try: 
    print(numbers[5])  
except IndexError:
    print("Indice fuera de rango.")
except TypeError:
    print("Tipo de dato invalido.")
else:
    print("Indice encontrado correctamente.")
finally:
    print("Gracias, vuelva pronto.")