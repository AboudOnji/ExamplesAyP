# Ejercicio 20: Juego de selección con match-case
# Escribe un programa que permita a 10 jugadores elegir entre tres juegos diferentes (A, B, C).
# Utiliza una estructura match-case para solicitar que el usaurio elija un juego
# El programa debe saludar al jugador por su nombre y confirmar su elección,
# Al finalizar muestra un conteo de cuántos jugadores eligieron cada juego.
ContA = ContB = ContC = 0
for i in range(1,11):
    name = input("Ingrese su primer nombre: ")
    opcion = input("Elige que juego quieres jugar (A), (B) o (C):")
    match opcion:
        case "A":
            print(f"Hola {name}, bienvenido al juego A")
            ContA += 1
        case "B":
            print(f"Hola {name}, bienvenido al juego B")
            ContB += 1
        case "C":
            print(f"Hola {name}, bienvenido al juego C")
            ContC += 1
        case _:
            print("Opción no válida, por favor elige A, B o C")
            break
print(f"Total de jugadores en el juego A: {ContA}")
print(f"Total de jugadores en el juego B: {ContB}")
print(f"Total de jugadores en el juego C: {ContC}")
# Ejercicio 20: Juego de selección con match-case