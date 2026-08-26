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

### Programa ###

while True:
    print("Consulte el stock del libro.")

    consulta = input("Ingrese el título del libro (0 para salir): ").strip()

    if consulta == "0":
        print("Gracias por utilizar nuestro sistema.")
        break

    if consulta in libros:
        print(f"El libro ingresado se encuentra en stock.\nTiene {libros[consulta]} unidades.")
        agrega_stock = input("Digite la cantidad de unidades a agregar: ").strip()

        while not agrega_stock.isdigit():
            print("Dato invalido. La cantidad a agregar debe ser un número.")
            agrega_stock = input("Digite la cantidad de unidades a agregar: ").strip()

        libros[consulta] += int(agrega_stock)
        print("Cantidad agregada.")

    else:
        libros.update({consulta: 0})
        print("El libro no se encontraba en sistema. Ya ha sido agregado.")

     


