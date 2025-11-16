# sets de estudiantes que aprobaron cada parcial
parcial1 = {"Juan", "Ana", "Pedro", "Lucía"}
parcial2 = {"Ana", "Carlos", "Pedro", "María"}

# estudiantes que aprobaron los 2 parciales
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# estudiantes que aprobaron solo 1
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

# estudiantes que aprobaron al menos 1 parcial
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)
