### FUNCIONES ###

def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime la información personal"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

### PROGRAMA ###

#Mensaje de bienvenida
print("Bienvenido al sistema de recolección de información Gran Hermano. Ingrese los datos solicitados.\n")
#Se solicita los datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su recidencia: ")

#Se llama a la funcion y se pasan los datos recolectados como parametros
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
