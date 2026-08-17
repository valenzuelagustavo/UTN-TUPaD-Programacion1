"""
TP integrador – Repetitivas- Condicionales y Secuenciales.

Ejercicio 1— “Caja del Kiosco”

Objetivo: Simular una compra con validaciones y cálculo de total.
"""

#Inicializo variables que utilizare en los inputs
nombre_cliente, cantidad_productos, precio, tiene_descuento = "", "", "", ""
#Acumuladores y auxiliares
total_con_descuento, total_sin_descuento, ahorro_total, promedio_por_producto = 0, 0, 0, 0
productos = []                  #Utilizo una lista para almacenar los precios
descuento_si_no = []            #Utilizo una lista para almacenar las 's' o 'n' del descuento

#Se pide el nombre del cliente
nombre = input("Ingrese el nombre del cliente: ").strip()
#Si no es alpha se pide nuevamente el nombre
while nombre.isalpha() == False:
    print("Nombre invalido.")
    nombre = input("Ingrese el nombre del cliente: ").strip().lower()

#Se piden la cantidad de productos
cantidad_productos = input("Ingrese la cantidad de productos: ").strip()
#Se valida que la cantidad sea un digito y además que sea mayor a 0
while cantidad_productos.isdigit() == False or int(cantidad_productos) <= 0:
    print("Cantidad no valida.")
    cantidad_productos = input("Ingrese la cantidad de productos: ").strip()
#Se pasa la cantidad de productos a entero 
cantidad_productos = int(cantidad_productos)

#Se solicitan los precios y si aplica descuento
for producto in range(1, cantidad_productos + 1):
    precio = input(f"Ingrese el precio del producto {producto}: ").strip()
    #Se valida que el precio sea un digito mayor a 0
    while precio.isdigit() == False or int(precio) <= 0:
        print("El precio ingresado no es valido.")
        precio = input(f"Ingrese el precio del producto {producto}: ").strip()
    #Luego de realizadas las validaciones se transforma el precio a entero
    precio = int(precio)
    #Se pregunta si el producto tiene descuento
    tiene_descuento = input("¿El producto tiene descuento? S/N: ").strip().lower()
    #Se valida si corresponde a una "s" o "n" lo ingresado
    while tiene_descuento != "s" and tiene_descuento != "n":
        print("Ingreso invalido. Debe ingresar unicamente S/N.")
        tiene_descuento = input("¿El producto tiene descuento? S/N: ").strip().lower()

    #Añado a las listas tanto el precio como si tenia descuento o no el producto
    descuento_si_no.append(tiene_descuento)
    productos.append(precio)
    #Se acumula el precio sin descuento
    total_sin_descuento += precio
    #Compruebo y aplico el descuento para el acumulador de Total con descuento
    if tiene_descuento == "s":
        total_con_descuento += (precio * 0.9)
    else:
        total_con_descuento += precio
#Imprimo por pantalla la información completa
print("---------------------------------------")
print(f"Cliente: {nombre.title()}")
print(f"Cantidad de productos: {cantidad_productos}")
for i in range(cantidad_productos):
    print(f"Producto {i+1} - Precio: {productos[i]}  Descuento (S/N): {descuento_si_no[i]}")
print("\n")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${total_sin_descuento - total_con_descuento:.2f}")
print(f"Promedio por producto: ${total_con_descuento / cantidad_productos:.2f}")
    

