"""
✅ Ejercicio 3 (Alta) — “Agenda de Turnos con 
Nombres (sin listas)” 
Contexto 
Hay 2 días de atención: Lunes y Martes. 
Cada día tiene cupos fijos: 
• Lunes: 4 turnos 
• Martes: 3 turnos 

"""
### VARIABLES ###
#Almacena el día
dia = ""
#Las variables que van a almacenar el nombre de los pacientes
lunes_1, lunes_2, lunes_3, lunes_4 = "", "", "", ""
martes_1, martes_2, martes_3 = "", "", ""
#Contadores para llevar la cuenta númerica de los turnos tomados
cont_lunes, cont_martes = 0, 0
#Nombre del paciente
nombre_paciente = ""

### INGRESO OPERARIO ###

nombre_operario = input("Ingrese nombre del operario: ").strip()
#Validamos que el nombre cumpla la condición y sino lo pedimos nuevamente
while not nombre_operario.isalpha():
    print("Nombre invalido. Por favor no utilice números ni caracteres especiales.")
    nombre_operario = input("Ingrese nombre del operario: ").strip()

### MENÚ ###

while True:
    print("""
    1. Reservar turno 
    2. Cancelar turno (por nombre) 
    3. Ver agenda del día 
    4. Ver resumen general 
    5. Cerrar sistema 
    """)
    #Pedimos que se elija la opción del menú
    opcion = input("Ingrese la opción elegida: ").strip()
    #Validamos la elección
    while not opcion.isdigit() or int(opcion) > 5 or int(opcion) == 0:
        print("Opción no valida.")
        opcion = input("Ingrese la opción elegida: ").strip()

    if opcion == "1":
        dia = input("Ingrese el día del turno a reservar (1=Lunes, 2=Martes): ").strip()
        while dia != "1" and dia != "2":
            print("Error: Entrada invalida.")
            dia = input("Ingrese el día del turno a reservar (1=Lunes, 2=Martes): ").strip()

        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()

        while not nombre_paciente.isalpha():
            print("El nombre no debe tener números ni caracteres especiales.")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        if dia == "1":
            if nombre_paciente == lunes_1 or nombre_paciente == lunes_2 or nombre_paciente == lunes_3 or nombre_paciente == lunes_4:
                print("El paciente ya tiene un turno este día.")
                continue
            if lunes_1 == "":
                lunes_1 = nombre_paciente
                cont_lunes += 1
            elif lunes_2 == "":
                lunes_2 = nombre_paciente
                cont_lunes += 1
            elif lunes_3 == "":
                lunes_3 = nombre_paciente
                cont_lunes += 1
            elif lunes_4 == "":
                lunes_4 = nombre_paciente
                cont_lunes += 1
            else:
                print("El día lunes ya se encuentra completo.")
        elif dia == "2":
            if nombre_paciente == martes_1 or nombre_paciente == martes_2 or nombre_paciente == martes_3:
                print("El paciente ya tiene un turno este día.")
                continue
            if martes_1 == "":
                martes_1 = nombre_paciente
                cont_martes += 1
            elif martes_2 == "":
                martes_2 = nombre_paciente
                cont_martes += 1
            elif martes_3 == "":
                martes_3 = nombre_paciente
                cont_martes += 1
            else:
                print("El día martes ya se encuentra completo.")
    elif opcion == "2":
        dia = input("Ingresar el día del turno a cancelar (1=Lunes, 2=Martes): ").strip()

        while dia != "1" and dia != "2":
            print("Error: Entrada invalida. (1=Lunes, 2=Martes):")
            dia = input("Ingresar el día del turno a cancelar (1=Lunes, 2=Martes):: ").strip()

        nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()
        while nombre_paciente.isalpha() == False:
            print("El nombre no debe tener números ni caracteres especiales.")
            nombre_paciente = input("Ingrese el nombre del paciente: ").strip().lower()

        if dia == "1":
            if nombre_paciente == lunes_1:
                lunes_1 = ""
                cont_lunes -= 1
                print("Turno borrado correctamente.")
            elif nombre_paciente == lunes_2:
                lunes_2 = ""
                cont_lunes -= 1
                print("Turno borrado correctamente.")
            elif nombre_paciente == lunes_3:
                lunes_3 = ""
                cont_lunes -= 1
                print("Turno borrado correctamente.")
            elif nombre_paciente == lunes_4:
                lunes_4 = ""
                cont_lunes -= 1
                print("Turno borrado correctamente.")
            else:
                print("El paciente no tiene turno asociado.")
        elif dia == "2":
            if nombre_paciente == martes_1:
                martes_1 = ""
                cont_martes -= 1
                print("Turno borrado correctamente.")
            elif nombre_paciente == martes_2:
                martes_2 = ""
                cont_martes -= 1
                print("Turno borrado correctamente.")
            elif nombre_paciente == martes_3:
                martes_3 = ""
                cont_martes -= 1
                print("Turno borrado correctamente.")
            else:
                print("El paciente no tiene turno asociado.")

    elif opcion == "3":
        dia = input("Ingrese el día que quiere consultar(1=Lunes, 2=Martes): ").strip()
        while dia != "1" and dia != "2":
            print("Error: Entrada invalida.")
            dia = input("Ingrese el día que quiere consultar(1=Lunes, 2=Martes): ").strip()

        if dia == "1":
            print("Los turnos tomados son: ")
            print(f"Turno 1: {lunes_1.title()}") if lunes_1 != "" else print ("Turno 1: libre")
            print(f"Turno 2: {lunes_2.title()}") if lunes_2 != "" else print ("Turno 2: libre")
            print(f"Turno 3: {lunes_3.title()}") if lunes_3 != "" else print ("Turno 3: libre")
            print(f"Turno 4: {lunes_4.title()}") if lunes_4 != "" else print ("Turno 4: libre")
        elif dia == "2":
            print("Los turnos tomados son: ")
            print(f"Turno 1: {martes_1.title()}") if martes_1 != "" else print ("Turno 1: libre")
            print(f"Turno 2: {martes_2.title()}") if martes_2 != "" else print ("Turno 2: libre")
            print(f"Turno 3: {martes_3.title()}") if martes_3 != "" else print ("Turno 3: libre")

    elif opcion == "4":
        print(f"El lunes tiene {cont_lunes} turnos asignados y {4 - cont_lunes} turnos libres.\nEl martes tiene {cont_martes} turnos asignados y {3 - cont_martes} turnos libres.")
        if cont_lunes == cont_martes:
            print("Ambos días tienen la misma cantidad de turnos. Hay empate.")
        elif cont_lunes > cont_martes:
            print(f"El lunes tiene {cont_lunes - cont_martes} más turnos asignados.") 
        elif cont_martes > cont_lunes:
            print(f"El martes tiene {cont_martes - cont_lunes} más turnos asignados.") 
    elif opcion == "5":
        print("Gracias por utilizar nuestro sistema de gestión.")
        quit()


        

                

