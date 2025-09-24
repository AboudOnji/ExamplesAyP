# Ejemplo12.py
# Este script demuestra el uso de varias funciones matemáticas en Python utilizando el módulo math.

import math

# --- Raíz cuadrada (sqrt) ---
numero = 81
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

# --- Potencia (pow) ---
base = 2
exponente = 3
potencia = math.pow(base, exponente)
print(f"{base} elevado a la {exponente} es: {potencia}")

# --- Redondeo hacia arriba (ceil) y hacia abajo (floor) ---
valor_decimal = 9.25
hacia_arriba = math.ceil(valor_decimal)
hacia_abajo = math.floor(valor_decimal)
print(f"El número {valor_decimal} redondeado hacia arriba es: {hacia_arriba}")
print(f"El número {valor_decimal} redondeado hacia abajo es: {hacia_abajo}")

# --- Factorial de un número (factorial) ---
n = 5
factorial_de_n = math.factorial(n)
print(f"El factorial de {n} es: {factorial_de_n}")