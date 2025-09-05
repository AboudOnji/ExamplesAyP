# Example7.py
# Juego de adivinar el número
# El programa elige un número entre 1 y 100
# El usuario intenta adivinar el número
# El programa indica si el número secreto es mayor o menor que el intento del usuario

numero_secreto = 42 # El número secreto es 42 (puede ser cualquier número entre 1 y 100).

# Inicializamos las variables.
intento_usuario = 0
contador_intentos = 0

# --- Lógica del juego ---
# Mensaje de bienvenida.
print("¡He pensado un número entre 1 y 100. Adivínalo!")

# El bucle se ejecuta mientras el intento del usuario NO sea igual al número secreto.
while intento_usuario != numero_secreto:

    # Pedimos al usuario que introduzca su intento.
    # La función int() convierte el texto que escribe el usuario en un número.
    intento_usuario = int(input("Introduce tu intento: "))

    # Aumentamos en 1 el contador de intentos.
    contador_intentos = contador_intentos + 1

    # Comparamos el intento con el número secreto usando condicionales if.
    if intento_usuario < numero_secreto:
        print("El número secreto es MAYOR.")
    elif intento_usuario > numero_secreto:
        print("El número secreto es MENOR.")

# --- Fin del juego ---
# Cuando el bucle termina, es porque el usuario adivinó.
# Mostramos el mensaje de felicitación.
print("¡Felicidades! Has adivinado el número.")
print("Lo hiciste en", contador_intentos, "intentos.")