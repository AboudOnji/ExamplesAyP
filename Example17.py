# Ejemplo17.py
# Este script implementa un cifrado César simple, desplazando cada caracter del mensaje original
# un numero fijo de posiciones en la tabla ASCII.
# -------------------------------------------------------------------------------------
# Pedimos al usuario el mensaje y el desplazamiento
mensaje_original = input("Introduce el mensaje a cifrar: ")
desplazamiento = int(input("Introduce el numero de desplazamiento (ej: 3): "))
# Creamos una cadena vacia para ir guardando el resultado
mensaje_cifrado = ""
# Recorremos cada letra en el mensaje original, una por una
for letra in mensaje_original:
    # Obtenemos el codigo numerico de la letra actual
    codigo_original = ord(letra)
    
    # Le sumamos el desplazamiento para obtener el nuevo codigo
    codigo_nuevo = codigo_original + desplazamiento
    
    # Convertimos el nuevo codigo de vuelta a un caracter
    letra_cifrada = chr(codigo_nuevo)
    
    # Anadimos la nueva letra cifrada a nuestro resultado
    mensaje_cifrado += letra_cifrada
print("Mensaje cifrado:", mensaje_cifrado)