### FUNCIONES ###
def tabla_multiplicar(numero):
    """Imprime la tabla del 1 al 10 del número pasado"""
    for n in range(1, 11):
        print(f"\t{numero} x {n} = {numero * n}")

### PROGRAMA ###

print("----- TABLAS DE MULTIPLICAR AUTOMATICAS ------\n")
#Pedimos el número para generar la tabla
numero_usuario = int(input("Ingrese el número para generar la tabla: "))

print(f"\n----- TABLA del {numero_usuario} -----\n")
#Llamamos a la función pasando el número como parametro
tabla_multiplicar(numero_usuario)
