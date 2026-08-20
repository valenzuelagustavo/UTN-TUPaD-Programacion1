#Ejercicio 2

### FUNCIONES ###
def saludar_usuario(nombre):
    """Imprime un saludo personalizado"""
    return f"Hola {nombre}!"

### PROGRAMA ###

#Se pide el nombre de usuario
nombre_usuario = input("Ingrese su nombre y reciba su saludo personalizado: ").strip()

#Se llama a la funcion y se pasa el nombre ingresado como parametro y se imprime por pantalla
print(saludar_usuario(nombre_usuario))