# Ejemplo 28: Promedio de calificaciones
# Cada sublista representa las calificaciones de un estudiante

calificaciones_grupo = [
    [10, 9, 10],
    [8, 7, 8],
    [9, 9, 10]
]

for i in range (len(calificaciones_grupo)):
    suma_de_notas = 0 
    for j in range (len(calificaciones_grupo[i])):
        suma_de_notas += calificaciones_grupo[i][j]
    promedio = suma_de_notas / len(calificaciones_grupo[i])
    print(f"Promedio del Estudiante {i + 1}: {promedio:.2f}")
