"""
Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
Objetivo: Login con intentos + menú de acciones con validación estricta.

"""

import random       #Utilizo la libreria random para que la frase que muestre sea al azar

###   VARIABLES   ###
usuario_correcto = "alumno"
clave_correcta = "python123"
opcion = 0
#La lista frases contiene frases cortas
frases = ["Cree que puedes y ya estás a medio camino.", "Cae siete veces, levántate ocho.", "Nunca es demasiado tarde para ser lo que podrías haber sido.", "La disciplina es el puente entre las metas y los logros.", "Hecho es mejor que perfecto."]

###   LOGIN DE USUARIO   ###   
#Se maneja la cantidad de intentos, más de 3 bloquean la cuenta
for i in range(1,4):
    usuario_intento = input(f"Intento {i}/3: Usuario: ")
    clave_intento = input("Clave: ")
    #Se valida que ambos, usuario y clave, sean correctos
    if usuario_intento == usuario_correcto and clave_intento == clave_correcta:
        print("Acceso concedido.\n")
        break
    else:
        #Se notifica al usuario que ha ingresado mal las credenciales
        print("Error: credenciales inválidas.")
    #Se valida que la cantidad de intentos este dentro del rango
    if i >= 3:
        print("Cuenta bloqueada")
        quit()
        
###   MENÚ PRINCIPAL   ###
while True:
    #Se muestran las opciones 
    print("1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")

    opcion = input("Opción: ")

    #Se valida que la opción sea un digito y sino se vuelve a iterar el bucle
    if opcion.isdigit() == False:
        print("ingrese un número válido.")
        continue
    #Validado que sea digito, se valida que este dentro del rango de opciones del menú
    if int(opcion) <= 0 or int(opcion) >= 5:
        print("Error: opción fuera de rango.")
        continue

    ##   OPCIONES DEL MENÚ   ##
    if opcion == "1":
        print("Inscripto")
        
    elif opcion == "2":
        while True:
            nueva_clave = input("Ingrese la nueva clave: ")
            #Se valida que la longitud de la clave no sea menor a 6
            if len(nueva_clave) < 6:
                print("La clave debe tener un mínimo de 6 caracteres.")
                continue
            #Se pide que se repita la nueva clave ingresada
            confirmacion_clave = input("Repita la nueva clave: ")
            #Se valida que ambos ingresos sean iguales
            if nueva_clave != confirmacion_clave:
                print("Error de verificación.")
                continue
            break
        #Se asigna la nueva clave a la clave correcta
        clave_correcta = nueva_clave
        #Se le da mensaje de confirmación al usuario
        print("Clave cambiada exitosamente.")
    elif opcion == "3":
        #Se usa choises() de la libreria random para mostrar una frase al azar de la lista de frases
        frases_random = random.choice(frases)
        print(frases_random)
        
    elif opcion == "4":
        #Imprime mensaje de despedida y cierra el programa
        print("Gracias por su visita.")
        break




