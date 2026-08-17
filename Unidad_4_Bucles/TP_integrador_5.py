#Variables
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
enemy_damage = 12
primer_turno = True
#Interfaz retro porque nunca está demas
print(r"""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║       ___ ___ ___   _   _ __  ___    ___  ___  ___  __  __                 ║
║      | __/ __/ __| /_\ | '_ \| __|  | _ \/ _ \/ _ \|  \/  |                ║
║      | _|\__ \ (__/ _ \| |_) | _|   |   / (_) | (_) | |\/| |               ║
║      |___|___/\___/_/ \_\ .__/|___|  |_|_\___/ \___/|_|  |_|               ║
║                         |_|                                                ║
║                                                                            ║
║  ========================================================================  ║
║                                                                            ║
║              ~ L A   A R E N A   D E L   G L A D I A D O R ~               ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                                                                            ║
║                  * POWERED BY 16 BIT BLAST PROCESSING  *                   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
""")
#Pequeña intro para ponernos en contexto
print("""Eones han pasado desde que fuiste arrebatado por el dictador de la republica de Gastpopía. 
Pero hoy es el día en que reclamaras tu venganza. El primer paso en tu cruzada es ganar,
aquí donde otras veces has derramado la sangre de tus enemigos.
Ya escuchas los vitores de tu nombre en las gradas. Los desprecias,
como desprecias al emperador que te traiciono.  
Pero eso ya no importa, hoy ganaras, hoy mataras, hoy conquistaras. 
Al pisar la arena gritas tu nombre...""")
#Pedimos el nombre del gladiador
nombre_gladiador = input("Ruges tu nombre mirando al cielo: ").strip()
#Validamos la entrada
while not nombre_gladiador.isalpha():
    nombre_gladiador = input("Tu garganta debe estar seca, vuelves a gritar tu nombre: ").strip()
#Bucle del juego con condición de salida
while vida_gladiador > 0 and vida_enemigo > 0:
    #Compruebo si estoy en el primer turno para ajustar la interfaz
    if primer_turno: print("\n=== INICIO DEL COMBATE ===")
    elif not primer_turno: print("\n===   NUEVO TURNO   ===")
    #Pequeño HUD con el HP de los contendientes y las pociones restantes.
    print(f"{nombre_gladiador.title()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo})  | Pociones: {pociones} ")
    print("""
    Elige acción:
    1. Ataque Pesado
    2. Ráfaga Veloz
    3. Curar
    """)
    #Se pide la opción de acción
    opcion = input("Opción: ").strip()
    #Validamos que se ajuste al número válido
    while not opcion.isdigit() or not opcion in ["1", "2", "3"]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ").strip()
    #Ataque pesado
    if opcion == "1":
        if vida_enemigo < 20:
            vida_enemigo = vida_enemigo - (ataque_pesado * 1.5)
            print(f"¡Atacaste al enemigo por {ataque_pesado * 1.5:.2f} puntos de daño!")
        else:
            vida_enemigo -= ataque_pesado
            print(f"¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
    #Ataque de ráfaga
    elif opcion == "2":
        for i in range(3):
            vida_enemigo -= 5
            print("Golpe conectado por 5 de daño")
    #Acción de tomar la poción
    elif opcion == "3":
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            if vida_gladiador > 100: vida_gladiador = 100
        elif pociones == 0:
            print("¡No te quedan más pociones!")
    if vida_enemigo > 0:
        vida_gladiador -= enemy_damage
        print("¡El enemigo te atacó por 12 puntos de daño!")
    #Seteamos el primer turno en False para el cambio de interfaz
    primer_turno = False

#Ya fuera del bucle comprobamos la condición de victoria o derrota
if vida_enemigo <= 0:
    print(f"¡VICTORIA! {nombre_gladiador.title()} ha ganado la batalla."  )
elif vida_gladiador <= 0:
    print("DERROTA. Has caído en combate." )
            

