### Ejercicio 9 ###
"""Organizador personal de eventos diarios que almacena actividades asociadas a un día y horario específico, permitiendo consultas exactas."""

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
consulta_hora = input("Ingrese la hora (HH:MM): ").strip()
dia_hora = (consulta_dia, consulta_hora)
actividad = agenda.get(dia_hora)
if actividad:
    print(f"Actividad: {actividad}")
else:
    print("El día y hora no tienen actividades.")