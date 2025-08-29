# Example2.py
# Calcula el factorial de un número
# Asegura que el número no sea negativo
# Si el número es 0, el factorial es 1

N = input("ingresa un número que no sea negativo: ")
N = int(N)
factorial = 1
if N < 0:
    print("el número no puede ser negativo")
elif N == 0:
    print("el factorial de 0 es 1")
else:
    for i in range(1, N+1):
        factorial = factorial * i
    print("el factorial de", N, "es", factorial)