#Ejercicio 9

#### FUNCIONES ###

def celsius_a_fahrenheit(celsius):
    """Devuleve la temperatura en Fahrenheit"""
    return (celsius * 1.8) + 32

### PROGRAMA ###

#Solicitamos al usuario la temperatura a convertir
temperatura = int(input("Ingrese la temperatura en ° Celsius: "))

#Mostramos la temperatura en °F
print(f"La temperatura en grados fahrenheit es {celsius_a_fahrenheit(temperatura)}° F")