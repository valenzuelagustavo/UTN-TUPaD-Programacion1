### EJERCICIO 2 ###

lista_productos = []
eliminar = ""
#Pedimos al usuario que ingrese 5 productos a la lista
for producto in range(5):
    lista_productos.append(input(f"Ingrese el producto N° {producto + 1} a la lista: "))

#Asignamos la lista ordenada a lista_ordenada
lista_ordenada = sorted(lista_productos)
#Asignamos a la variable resultado los elementos de la lista ordenada separados por ',' solamente con fines visuales
resultado = ", ".join(lista_ordenada)
#Se muestran los elementos de la lista ordenada
print(f"La lista ordenada: {resultado}")

while True:
    #Preguntamos si quiere eliminar algún elemento
    eliminar = input("¿Cual queres eliminar? (0 para salir.): ")
    if eliminar == "0": break #Si elige '0' Salimos del bucle
    #Se comprueba que el elemento este en la lista
    if eliminar not in lista_ordenada:
        print("Dato invalido. El articulo no se encuentra en la lista.")
        continue   

    #Eliminamos el elemento 
    lista_ordenada.remove(eliminar)    
    lista_acortada = ", ".join(lista_ordenada)
    #Mostramos la lista ordenada sin el elemento eliminado
    print(f"La lista ordenada actualizada: {lista_acortada}")
    
#Saludo de despedida
print("¡Hasta pronto!")



