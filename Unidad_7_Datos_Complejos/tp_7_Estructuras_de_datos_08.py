### Ejercicio 8 ###

libros = {
    "El principito": 2,
    "Mafalda 10": 1,
    "Aventuras de Sherlock Holmes": 10,
    "Fahrenheit 451": 1,
    "Batman - La broma asesina": 4,
    "1984": 3,
    "It": 1,
    "Salem's Lot": 3,
    "El padrino": 1,
}

while True:
    print("Consulte el stock del libro.")

    consulta = input("Ingrese el título del libro: ").strip()

    if consulta in libros:
        print("El libro se encuentra en nuestro inventario.")
    else:
        print("El libro no se encuentra en nuestro catalogo.")

    opcion = input("¿Quiere agregar stock [1] o agregar un producto [2]?\nElija la opción: ")

    while opcion not in ["1", "2"]:
        print("Opción invalida.")
        opcion = input("¿Quiere agregar stock [1] o agregar un producto [2]?\nElija la opción: ")

    if opcion == "2":
        nuevo_producto = input("Ingrese el título del nuevo libro: ")
        cantidad_libro = input("Ingrese la cantidad de unidades: ")

        libros.update({nuevo_producto: cantidad_libro})



