#Ejercicio 8

### FUNCIONES ###

def calcular_imc(peso, altura):
    """Calcula y devuelve el IMC"""
    return peso / (altura ** 2)

#Agregados no pedidos en consigna. Los dejo comentados.
#def estado_peso_corporal(imc):
#    """Devuelve el estado de peso corporal segun IMC"""
#    if imc >= 40: print("Usted tiene Obesidad Grado III")
#    elif 35 <= imc < 40: print("Usted tiene Obesidad Grado II")
#    elif 30 <= imc < 35: print("Usted tiene Obesidad Grado I")
#    elif 25 <= imc < 30: print("Usted tiene Sobrepeso")
#    elif 18.5 <= imc < 25: print("Usted tiene Peso normal")
#    elif imc < 18.5: print("Usted tiene Bajo peso")

#def imprimir_tabla_imc():
#    """Imprime la tabla de IMC"""
#    print("""
#+----------------------+--------------------+
#| Clasificación        | IMC (kg/m2)        |
#+----------------------+--------------------+
#| Bajo peso            | Menos de 18,4      |
#| Peso normal          | 18,5 a 24,9        |
#| Sobrepeso            | 25 a 29,9          |
#| Obesidad Grado I     | 30 a 34,9          |
#| Obesidad Grado II    | 35 a 39,9          |
#| Obesidad Grado III   | Igual o mayor a 40 |
#+----------------------+--------------------+
#""")

### PROGRAMA ###

#Introducción respecto al IMC
print("----- CALCULADORA DE Índice de Masa Corporal (IMC) -----")
print("El Índice de Masa Corporal (IMC) es una herramienta utilizada por \nprofesionales de la salud para estimar la cantidad de grasa corporal a partir de la relación entre el peso y la altura. \nSirve como una evaluación inicial para identificar si una persona tiene un peso adecuado, bajo o elevado.")

#Se le pide al usuario los datos
peso_usuario = float(input("Ingrese su peso (en Kg.): ").strip())
altura_usuario = float(input("Ingrese su altura (en metros): ").strip())
#Se guarda el resultado de la funcion en una variable para pasarla como parametro en otra funcion
imc = calcular_imc(peso_usuario, altura_usuario)
#Se muestra el IMC del usuario
print(f"Su IMC es de {imc:.2f}")

#Agregados no pedidos en consigna. Los dejo comentados.
#Se consulta si quiere información adicional
#informacion = input("¿Quiere saber más información? (SI / NO): ").strip().lower()
#Comprobación de respuesta
#while informacion not in ["si", "no"]:
#    print("Entrada invalida.")
#    informacion = input("¿Quiere saber más información? (SI / NO): ").strip().lower()
#Se muestra la información con dos funciones
#if informacion == "si":
#    estado_peso_corporal(imc)
#    imprimir_tabla_imc()
#else:
    #Si no quiere ver la información se le da un consejo, que no viene mal.
#    print("No se preocupe, pero acuda al doctor ante cualquier duda.")






