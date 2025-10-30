# Este código ordena una lista de listas usando el algoritmo de burbuja.
calificaciones = [
    [8, 5, 10, 7],
    [9, 9, 6, 8],
    [10, 7, 7, 9]
]
print("Calificaciones antes de ordenar:")
for fila in calificaciones:
    print(fila)
    
for fila in calificaciones:
    n = len(fila)
    for i in range(n):
        for j in range(n-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

print("Calificaciones después de ordenar:")
for fila in calificaciones:
    print(fila)