#Ejercicio 6

### FUNCIONES ###
def tabla_multiplicar(numero):
    """Imprime la tabla del 1 al 10 del número pasado"""
    for n in range(1, 11):
        print(f"\t{numero} x {n} = {int(numero) * n}")

def es_entero_positivo(entrada):
    """Verifica que la entrada sean solo digitos"""
    return entrada.isdigit() 

### PROGRAMA ###

print("----- TABLAS DE MULTIPLICAR AUTOMATICAS ------\n")
#Pedimos el número para generar la tabla
numero_usuario = input("Ingrese el número para generar la tabla: ")
while not es_entero_positivo(numero_usuario):
    print("Dato invalido. Debe ser mayor o igual a 0.")
    numero_usuario = input("Ingrese el número para generar la tabla: ")

print(f"\n----- TABLA del {numero_usuario} -----\n")
#Llamamos a la función pasando el número como parametro
tabla_multiplicar(numero_usuario)
