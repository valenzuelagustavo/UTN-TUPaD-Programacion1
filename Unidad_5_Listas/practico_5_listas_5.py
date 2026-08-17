### Ejercicio 5 ###
#Lista de estudiante
lista_estudiantes = ["Andres", "Gonzalo", "Carla", "Matias", "Ivan", "Bernardo", "Aldana", "Matias"]

while True:
    #Pedimos al usuario que elija si agregar o eliminar un estudiante
    opcion = input("¿Desea agregar(A) o eliminar(E) algún estudiante?(0 para salir): ").strip().lower()
    #Si pulsa 0 sale del bucle 
    if opcion == "0": break
    #Valido que la opción sea una de las dos posibilidades
    if opcion not in ["a", "e"]:
        print("Dato invalido.")
        continue
    #Opción de agregar alumno
    if opcion == "a":
        ingreso = input("Ingrese el nombre del nuevo estudiante: ")   #Pedimos el ingreso del nuevo alumno
        lista_estudiantes.append(ingreso)      #Se lo añadimos a la lista
        print(f"La lista de estudiantes actualizada es: {lista_estudiantes}")    #Muestro la lista actualizada
    #Opción de eliminar un alumno
    elif opcion == "e":
        salida = input("Ingrese el nombre del alumno a eliminar: ")    #Pedimos el nombre a eliminar
        #Si el nombre no se encuentra en la lista volvemos al principio del bucle
        if salida not in lista_estudiantes:     
            print("El alumno no se encuentra en la lista")
            continue
        #Si el nombre se encuentra en la lista procedo a removerlo
        elif salida in lista_estudiantes:
            lista_estudiantes.remove(salida)
            print(f"La lista de estudiantes actualizada es: {lista_estudiantes}")   #Muestro la lista acutualizada

print("¡Hasta luego!")     #Mensaje de despedida