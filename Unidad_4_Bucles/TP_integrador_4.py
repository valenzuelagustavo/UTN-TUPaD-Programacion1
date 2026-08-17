"""
Ejercicio 4  — “Escape Room: La Bóveda” 
Historia 
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
limitados. 
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. 

"""

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_spam = 0
alarma_encendida = "Encendida"
alarma_apagada = "Apagada"
### HISTORIA ###
print("\tESCAPE ROOM: LA BÓVEDA\n\nSos un agente que intenta abrir una bóveda con 3 cerraduras.\n Tenés energía y tiempo limitados.\n Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. ")
### INGRESO DE AGENTE ###

nombre_agente = input("Ingrese el nombre del agente: ").strip()

while not nombre_agente.isalpha():
    print("Error. El nombre del agente es invalido.")
    nombre_agente = input("Ingrese el nombre del agente: ").strip()

### JUEGO ###

while True:
    print("""

    -------------------------------------------------------------------------
    1. Forzar cerradura (costo: -20 energía, -2 tiempo) 
    2. Hackear panel (costo: -10 energía, -3 tiempo) 
    3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 
    energía extra) 
    -------------------------------------------------------------------------
    """)
    #Ajuste de interfaz según estado de alarma
    print(f"Energia: {energia}   Tiempo: {tiempo}   Alarma:{alarma_encendida}\n") if alarma else print (f"Energia: {energia}   Tiempo: {tiempo}   Alarma:{alarma_apagada}\n")
    #Se muestra el codigo parcial decifrado si
    print(f"CODIGO PARCIAL: {codigo_parcial}\n")

    #Se pide la opción 
    opcion = input("Elija la opción (1, 2 o 3): ").strip()
    #Validacion de la opción
    while not opcion.isdigit() and not opcion in ["1", "2", "3"]:
        print("Error. La opción debe ser 1, 2 o 3.")
        opcion = input("Elija la opción (1, 2 o 3): ").strip()
        if opcion not in ["1", "2", "3"]:
            continue

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        anti_spam += 1
        if energia < 40:
            riesgo_alarma = input("Hay riesgo de alarma, debes elegir entre los números 1, 2 o 3: ").strip()
            while not riesgo_alarma.isdigit() or riesgo_alarma not in ["1", "2", "3"]:
                riesgo_alarma = input("Hay riesgo de alarma, debes elegir entre los números 1, 2 o 3: ").strip()
            if riesgo_alarma == "3": alarma = True
        if anti_spam == 3: alarma = True
        if alarma == False: cerraduras_abiertas += 1
            
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        anti_spam = 0
        for i in range(4):
            codigo_parcial += "A"
            print(f"Descifrando código: {codigo_parcial}")
        if cerraduras_abiertas <= 3:
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
    elif opcion == "3": 
        anti_spam = 0
        tiempo -= 1     
        energia += 15
        if energia > 100: energia = 100        
        if alarma: energia -= 10

    if cerraduras_abiertas == 3:
        print("¡VICTORIA! ¡USTED ES UN VERDADERO AGENTE DEL RECONTRA ESPIONAJE!")
        break
    elif energia <= 0 or tiempo <= 0:
        print("¡DERROTA! ¡UNA NUEVA VICTORIA PARA KAOS!")
        break
    elif alarma == True and tiempo <= 3:
        print("¡DERROTA! ¡CONTROL JAMÁS TUVO OPORTUNIDAD!")
        break


