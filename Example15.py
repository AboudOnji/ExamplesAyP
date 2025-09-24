# Ejemplo15.py
# Este script decodifica un mensaje secreto utilizando indices para extraer caracteres de una cadena.
# La informacion oculta se encuentra en los caracteres de ciertas posiciones especificas.
# -------------------------------------------------------------------------------------
# El mensaje cifrado contiene la informacion oculta
mensaje_cifrado = "aPzYleTtnHhOoNnlax"
# Estos son los indices de los caracteres correctos
indices_secretos = [1, 3, 6, 9, 11, 13]
# Variable para guardar el resultado, comienza vacia
mensaje_decodificado = ""
# 1. Creamos un bucle 'for' que recorra cada numero en la lista 'indices_secretos'.
#    En la primera iteracion, 'indice' valdra 1, en la segunda 5, y asi sucesivamente.
for indice in indices_secretos: 
    
    # 2. Usamos el 'indice' actual para extraer el caracter correspondiente
    #    del 'mensaje_cifrado'.
    caracter_secreto = mensaje_cifrado[indice]
    
    # 3. Anadimos (concatenamos) el caracter extraido al final de nuestro
    #    mensaje decodificado.
    mensaje_decodificado += caracter_secreto
# Al final, imprimimos el mensaje decodificado completo
print("El mensaje secreto es:", mensaje_decodificado)