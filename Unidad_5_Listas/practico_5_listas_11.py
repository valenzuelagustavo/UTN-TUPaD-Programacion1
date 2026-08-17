### EJERCICIO 11 ###

#Lista de estudiantes
estudiantes = ["carlos", "andrea", "martin", "tomas", "enrique", "gustavo", "gwen", "aldana", "nicolas", "sebastian"]

# Bucle del sistema de búsqueda
while True:
    print("Bienvenido al sistema de búsqueda de estudiantes.")
    nombre = input("Ingrese el nombre para buscar (S para Salir): ").lower().strip() #Se pide el ingreso del usuario
    #Opción de salida del sistema
    if nombre == "s": 
        print("Gracias por utilizar nuestro sistema de búsqueda.")
        break
    # Si no se encuentra el nombre en la lista se avisa al usuario
    if nombre not in estudiantes:
        print("El estudiante no se encuentra en la lista.")
        continue
    #Si el nombre se encuentra en la lista
    elif nombre in estudiantes:
        for match in range(len(estudiantes)):   #Recorremos la lista buscando la posición del match
            if estudiantes[match] == nombre:
                #Informamos la posición ajustandola para que no confunda el indice sumandole 1
                print(f"Nombre encontrado. La posición en la lista es {match + 1}.")  
