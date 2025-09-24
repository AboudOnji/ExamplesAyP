import math

# --- Uso de constantes (pi y e) ---
print(f"El valor de Pi (π) es: {math.pi}")
print(f"El valor de Euler (e) es: {math.e}")

# Ejemplo: Calcular el área de un círculo
radio = 5
area_circulo = math.pi * (radio ** 2) # o math.pi * math.pow(radio, 2)
print(f"El área de un círculo con radio {radio} es: {area_circulo:.2f}")

# --- Logaritmos ---
# Logaritmo natural (base e)
valor = 10
logaritmo_natural = math.log(valor)
print(f"El logaritmo natural de {valor} es: {logaritmo_natural:.2f}")

# Logaritmo en base 10
logaritmo_base10 = math.log10(valor)
print(f"El logaritmo base 10 de {valor} es: {logaritmo_base10}")

# Logaritmo en otra base (ej. base 2)
logaritmo_base2 = math.log(valor, 2)
print(f"El logaritmo base 2 de {valor} es: {logaritmo_base2:.2f}")