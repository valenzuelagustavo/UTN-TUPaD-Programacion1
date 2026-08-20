#Ejercicio 5

### FUNCIONES ###

def segundos_a_horas(segundos):
    """Pasa un número expresado en segundos a su equivalente en horas"""
    return segundos / 3600

### PROGRAMA ###

print("-- Conversor SEGUNDOS/HORAS --")
segundos_usuario = input("Ingrese la cantidad de segundos: ")
while not segundos_usuario.isdigit() or int(segundos_usuario) == 0:
    print("Ingreso invalido. Debe ser un número entero mayor a 0.") 
    segundos_usuario = input("Ingrese la cantidad de segundos: ")

print(f"La cantidad de {segundos_usuario} segundos corresponden a {segundos_a_horas(int(segundos_usuario))} horas.")