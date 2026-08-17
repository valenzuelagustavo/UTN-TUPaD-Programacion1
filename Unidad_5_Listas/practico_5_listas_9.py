ta_te_ti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

fila = 0
columna = 0
jugador_1=True

while True:
    if jugador_1:
        fila = input("Ingresa el número de fila (0, 1 o 2): ")
        if fila not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
            continue
        columna = input("Ingresa el número de columna (0, 1 o 2): ")
        if columna not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
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
        fila = input("Ingresa el número de fila (0, 1 o 2): ")
        if fila not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
            continue
        columna = input("Ingresa el número de columna (0, 1 o 2): ")
        if columna not in ["0", "1", "2"]: 
            print("Dato de columna invalido (0, 1 o 2).")
            continue
        if ta_te_ti[int(fila)][int(columna)]  == "-":
            ta_te_ti[int(fila)][int(columna)]  = "O"
        else:
            print("La casilla ya esta ocupada, elegir otra.")
            continue

        for planilla in ta_te_ti:
            print(planilla)
        jugador_1 = True



