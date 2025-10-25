Temp = [
    [10, 22],
    [12, 25],
    [8, 20],
    [15, 23],
    [13, 26],
    [11, 23],
    [9, 21]
]

suma_max = 0
suma_min = 0
amplitudmax=-1
diaamplitudmax=""

for dia in Temp:
    suma_min += dia[0]
    suma_max += dia[1]

prom_max = suma_max / len(Temp)
prom_min = suma_min / len(Temp)

print(f"promedio de maximas: {prom_max}")
print(f"promedio de minimas: {prom_min}")

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(len(Temp)):
    minima = Temp[i][0]
    maxima = Temp[i][1]
    amplitud_actual = maxima - minima

    if amplitud_actual > amplitudmax:
        amplitudmax = amplitud_actual
        diaamplitudmax = dias_semana[i]

print(f"El día con la mayor amplitud térmica ({amplitudmax}°C) fue: {diaamplitudmax}")