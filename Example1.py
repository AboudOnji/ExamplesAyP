# Example2.py
# Calcula el factorial de un número

N = input("ingresa un número que no sea negativo: ")
N = int(N)
factorial = 1
for i in range(1, N+1):
    factorial = factorial * i
print("el factorial de", N, "es", factorial)