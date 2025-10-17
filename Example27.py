# Ejemplo 27: Tablero de Gato
# Creamos una lista de listas para representar el tablero

tablero = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

tablero[1][1] = 'X'

print('Tablero de Gato:')
for fila in tablero:
    print(fila)
