#Ejercicio 3

### FUNCIONES ###

def informacion_personal(nombre, apellido, edad, residencia):
    """Imprime la información personal"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def es_entero_positivo(entrada):
    """Verifica que la entrada sean solo digitos y mayores a 0"""
    return entrada.isdigit() and int(entrada) > 0

### PROGRAMA ###

#Mensaje de bienvenida
print("Bienvenido al sistema de recolección de información Gran Hermano. Ingrese los datos solicitados.\n")
#Se solicita los datos al usuario
nombre_usuario = input("Ingrese su nombre: ").strip()
apellido_usuario = input("Ingrese su apellido: ").strip()
edad_usuario = input("Ingrese su edad: ").strip()
#Valido que la edad sea un número valido
while not es_entero_positivo(edad_usuario):
    print("Edad no valida. Debe ser un número mayor a 0.")
    edad_usuario = input("Ingrese su edad: ").strip()
residencia_usuario = input("Ingrese su residencia: ").strip()

#Se llama a la funcion y se pasan los datos recolectados como parametros
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
