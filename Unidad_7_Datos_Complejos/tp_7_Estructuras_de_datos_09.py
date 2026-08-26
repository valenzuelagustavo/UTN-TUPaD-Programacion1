### Ejercicio 9 ###

agenda = {
    ("lunes", "10:00"): "Consultas integrador",
    ("martes", "09:15"): "Consultas TP",
    ("miercoles", "15:00"): "Manejo de archivos",
    ("jueves", "09:00"): "Datos complejos",
    ("viernes", "14:30"): "Trabajo colaborativo",
    ("sabado", "07:00"): "Running",
    ("domingo", "11:30"): "Compras/Makro"
}

### Programa ###

print("Organizador personal de eventos diarios (A.K.A. Agenda)")

consulta_dia = input("Ingrese el día por el que quiere consultar: ").strip().lower()
consulta_hora = input("Ingrese la hora: ").strip()

for consulta_dia, consulta_hora in agenda.items():
    print(f"Actividad: {agenda.values}")