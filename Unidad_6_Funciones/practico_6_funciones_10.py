### FUNCIONES ###
def calcular_promedio(a, b, c):
    """Calcula el promedio de los tres números"""
    return (a + b + c) / 3

### PROGRAMA ### 

num_a = float(input("Ingrese el primer número: "))
num_b = float(input("Ingrese el segundo número: "))
num_c = float(input("Ingrese el tercer número: "))

print(f"El promedio de los tres números ingresados es {calcular_promedio(num_a, num_b, num_c):.2f}")