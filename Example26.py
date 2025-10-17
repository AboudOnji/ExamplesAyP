# Ejemplo 26: Triángulo de asteriscos
# Pedimos al usuario la altura del triángulo

altura = int(input("Introduce la altura del triangulo: "))
# Ciclo externo para cada fila
for fila in range(1, altura + 1):
    # Se ejecuta 'fila' veces
    for columna in range(fila):
        print("*", end="")
    print() # Salto de línea después de cada fila