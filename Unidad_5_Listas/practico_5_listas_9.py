### EJERCICIO 9 ###

ta_te_ti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

fila = 0
columna = 0
jugador_1=True     #Variable para intercambiar turnos entre ambos players
jugador_1_win = False
jugador_2_win = False

while True:
    #Analizo si algún player gano
    for tateti in ta_te_ti:
        if tateti[0] == tateti[1] == tateti[2] == "X":
            jugador_1_win = True
        elif tateti[0] == tateti[1] == tateti[2] == "O":
            jugador_2_win = True
    if ta_te_ti[0][0] == ta_te_ti[1][1] == ta_te_ti[2][2] == "X":
        jugador_1_win = True
    elif ta_te_ti[0][0] == ta_te_ti[1][0] == ta_te_ti[2][0] == "X":
        jugador_1_win = True
    elif ta_te_ti[0][1] == ta_te_ti[1][1] == ta_te_ti[2][1] == "X":
        jugador_1_win = True
    elif ta_te_ti[0][2] == ta_te_ti[1][2] == ta_te_ti[2][2] == "X":
        jugador_1_win = True
    if ta_te_ti[2][0] == ta_te_ti[1][1] == ta_te_ti[0][2] == "X":
        jugador_1_win = True
    elif ta_te_ti[0][0] == ta_te_ti[1][1] == ta_te_ti[2][2] == "O":
        jugador_2_win = True
    elif ta_te_ti[0][0] == ta_te_ti[1][0] == ta_te_ti[2][0] == "O":
        jugador_2_win = True
    elif ta_te_ti[0][1] == ta_te_ti[1][1] == ta_te_ti[2][1] == "O":
        jugador_2_win = True
    elif ta_te_ti[0][2] == ta_te_ti[1][2] == ta_te_ti[2][2] == "O":
        jugador_2_win = True
    if ta_te_ti[2][0] == ta_te_ti[1][1] == ta_te_ti[0][2] == "O":
        jugador_2_win = True


    #Muestro mensaje y salgo del bucle 
    if jugador_1_win:
        print("¡¡El jugador 1 ha ganado!!")
        break
    elif jugador_2_win:
        print("¡¡El jugador 2 ha ganado!!")
        break
    #Turno del jugador 1
    if jugador_1:
        print("--------Turno del jugador 1 (X)----------\n")
        fila = input("Ingresa el número de fila (0, 1 o 2): ")
        if fila not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
            continue
        columna = input("Ingresa el número de columna (0, 1 o 2): ")
        if columna not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).\n")
            continue
        if ta_te_ti[int(fila)][int(columna)] == "-":
            ta_te_ti[int(fila)][int(columna)]  = "X"
        else:
            print("La casilla ya esta ocupada, elegir otra.")
            continue
        
        for planilla in ta_te_ti:
            print(planilla)
        
        jugador_1 = False
    elif not jugador_1:
        print("--------Turno del jugador 2 (O)----------\n")
        fila = input("Ingresa el número de fila (0, 1 o 2): ")
        if fila not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
            continue
        columna = input("Ingresa el número de columna (0, 1 o 2): ")
        if columna not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).\n")
            continue
        if ta_te_ti[int(fila)][int(columna)]  == "-":
            ta_te_ti[int(fila)][int(columna)]  = "O"
        else:
            print("La casilla ya esta ocupada, elegir otra.")
            continue

        for planilla in ta_te_ti:
            print(planilla)
        jugador_1 = True

        for tateti in ta_te_ti:
            if tateti[0] == "X" and tateti[1] == "X" and tateti[2] == "X":
                jugador_1_win = True
            elif tateti[0] == "O" and tateti[1] == "O" and tateti[2] == "O":
                jugador_2_win = True

        if jugador_1_win:
            print("¡¡El jugador 1 ha ganado!!")
            break
        elif jugador_2_win:
            print("¡¡El jugador 2 ha ganado!!")
            break


