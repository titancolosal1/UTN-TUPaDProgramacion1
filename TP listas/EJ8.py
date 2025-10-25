notas = [[3, 5, 7], [9, 8, 9], [4, 6, 7], [8, 6, 8], [9, 5, 6]]
estudiantes = ["Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4", "Estudiante 5"]


for i in range(len(notas)):
    suma_notas = sum(notas[i])
    prom = suma_notas / len(notas[i])
    print(f"El promedio de {estudiantes[i]} es: {prom}")

materias = ["Materia 1", "Materia 2", "Materia 3"]

for i in range(len(notas[0])):
    suma_materia = 0
    
    for j in range(len(notas)):
        suma_materia += notas[j][i]
    
    promedio_materia = suma_materia / len(notas)
    print(f"El promedio de {materias[i]} es: {promedio_materia}")