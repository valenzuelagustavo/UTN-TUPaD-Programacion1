### FUNCIONES ###

def segundos_a_horas(segundos):
    """Pasa un número expresado en segundos a su equivalente en horas"""
    return segundos / 3600

### PROGRAMA ###

print("-- Conversor SEGUNDOS/HORAS --")
segundos_usuario = int(input("Ingrese la cantidad de segundos: "))
#TODO: Checkear temas de conversion horaria

print(f"La cantidad de {segundos_usuario} segundos corresponden a {segundos_a_horas(segundos_usuario)} horas.")