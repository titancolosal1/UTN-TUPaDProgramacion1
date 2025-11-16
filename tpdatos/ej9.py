agenda = {}

agenda[("Lunes", "10:00")] = "Desayuno con la flia"
agenda[("Martes", "18:30")] = "Juega Racing"
agenda[("Miércoles", "09:00")] = "Dentista"

for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

consulta = ("Martes", "18:30")
if consulta in agenda:
    print(f"\nEvento consultado: {agenda[consulta]}")
else:
    print("\nNo hay evento programado en ese día y hora.")
