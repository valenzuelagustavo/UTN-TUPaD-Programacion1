### EJERCICIO 10 ###

productos_semana = [
    [1200, 4200, 2500, 400, 850, 990, 460],
    [1650, 8800, 7200, 550, 220, 1500, 760],
    [590, 720, 360, 1000, 1050, 1060, 1090],
    [220, 1500, 760, 2230, 3060, 3070, 3090]
]
#VARIABLES
mas_vendido = 0   #Auxiliar para almacenar el producto más vendido
total_por_producto = []   #Lista para almacenar los totales por producto
suma_dia = [0] * len(productos_semana[0])   #Lista para almacenar la suma por día
dia_mas_ventas = 0                      #Auxiliar para almacenar el día con más ventas
#Recorremos los productos por día de semana
for producto in productos_semana:
    total = sum(producto)
    total_por_producto.append(total)  #Añadimos la suma de productos en la semana a la lista
    #Recorremos la lista por columnas para almacenar la suma del día
    for dia in range(len(producto)):    
        suma_dia[dia] += producto[dia]
#Recorremos y almacenamos el día con más venta
for dia in suma_dia:
    if dia > dia_mas_ventas:
        dia_mas_ventas = dia

#Buscamos el producto más vendido
for producto in total_por_producto:
    if producto > mas_vendido:
        mas_vendido = producto

print("Estadisticas: ")
for producto in range(len(total_por_producto)):
    print(f"-Total producto {producto + 1}: ${total_por_producto[producto]:.2f}")
#print(f"El día de mayor venta se registraron ${dia_mayor_venta:.2f}")
print(f"El día con más ventas se facturo ${dia_mas_ventas:.2f}")
print(f"El producto que registro más ventas facturo ${mas_vendido:.2f}")
