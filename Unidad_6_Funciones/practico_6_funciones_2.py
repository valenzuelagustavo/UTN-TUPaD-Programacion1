#Funciones
def saludar_usuario(nombre):
    """Imprime un saludo personalizado"""
    print(f"Hola {nombre}!")

#Programa

#Se pide el nombre de usuario
nombre_usuario = input("Ingrese su nombre y reciba su saludo personalizado: ")

#Se llama a la funcion y se pasa el nombre ingresado como parametro 
saludar_usuario(nombre_usuario)