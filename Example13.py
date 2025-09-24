# Ejemplo13.py
# Este script demuestra el uso de funciones trigonométricas en Python utilizando el módulo math.

import math

# --- Conversión de grados a radianes (radians) ---
angulo_grados = 90
angulo_radianes = math.radians(angulo_grados)
print(f"{angulo_grados} grados son {angulo_radianes:.4f} radianes.")

# --- Calcular el seno (sin), coseno (cos) y tangente (tan) ---
# Usamos el ángulo en radianes que calculamos antes
seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)

print(f"Seno de {angulo_grados}°: {seno}")
# El coseno de 90° debería ser 0, pero por la precisión de los flotantes,
# a veces da un número muy pequeño, cercano a cero.
print(f"Coseno de {angulo_grados}°: {round(coseno, 5)}")

# Ejemplo práctico: calcular la altura de un edificio
# Si tenemos un ángulo de 45° y una distancia de 20 metros
distancia = 20
angulo_edificio_grados = 45
angulo_edificio_radianes = math.radians(angulo_edificio_grados)
altura = distancia * math.tan(angulo_edificio_radianes)
print(f"La altura del edificio es de {altura:.2f} metros.")