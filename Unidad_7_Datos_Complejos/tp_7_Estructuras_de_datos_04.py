### Ejercicio 4 ###
"""Sistema interactivo de agenda telefónica que permite registrar contactos y consultar números guardados."""

contactos = {}

print("Sistema de Agenda\nAgregue 5 contactos y su número de telefono.")
for i in range(5):
    nombre = input("Ingrese el nombre: ").strip().lower()

    while not nombre.isalpha():
        print("El nombre no puede contener números ni caracteres especiales.")
        nombre = input("Ingrese el nombre: ").strip().lower()

    telefono = input("Ingrese el telefono: ").strip()

    while not telefono.isdigit(): 
        print("El telefono debe ser un número valido.")
        telefono = input("Ingrese el telefono: ").strip()
    contactos.update({nombre : telefono })



busqueda_nombre = input("Ingrese el nombre para buscarlo en la agenda: ").strip().lower()

if busqueda_nombre in contactos: 
    print(f"{busqueda_nombre.title()}: {contactos[busqueda_nombre]}")
else:
    print("El contacto no se encuentra en la agenda.")

