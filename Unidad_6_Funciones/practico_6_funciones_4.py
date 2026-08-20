import math

### FUNCIONES ###
def calcular_area_circulo(radio):
    """Calcula y devuelve el área de un círculo"""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Calcula y devuelve el área de un circulo"""
    return 2 * math.pi * radio

### PROGRAMA ###

#Pedimos el radio al usuario
radio_usuario = float(input("Ingrese el radio de un círculo: "))

#Mostramos los resultados llamando a las funciones pasandoles el radio como parametro
print(f"El área del círculo es {calcular_area_circulo(radio_usuario):.2f}, su perímetro es {calcular_perimetro_circulo(radio_usuario):.2f}.")

