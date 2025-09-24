# Ejemplo16.py
# Este script genera un recibo de compra formateado profesionalmente
# utilizando listas paralelas para almacenar productos y sus precios.
# -------------------------------------------------------------------------------------
# Listas paralelas: el producto en el indice 0 corresponde al precio en el indice 0, y asi sucesivamente.
productos = ["Leche Entera", "Pan de Caja", "Huevo (12pza)"]
precios = [25.50, 42.00, 38.95]
# Variable para acumular el total de la compra, comienza en cero.
total = 0.0
# --- 2. Impresion del Encabezado ---
print("--- RECIBO DE COMPRA ---")
print("No. | Producto        | Precio")
print("-------------------------------")
# 3. Bucle para recorrer las listas por indice
# range(len(productos)) genera una secuencia de numeros: 0, 1, 2
for i in range(len(productos)):
    
    # a. Acceder a los datos usando el indice 'i'
    numero_item = i + 1
    producto_actual = productos[i]
    precio_actual = precios[i]
    
    # b. Acumular el precio en el total
    total += precio_actual
    
    # c. Imprimir la linea del producto con formato profesional
    #    - :02d -> numero de 2 digitos con cero a la izquierda
    #    - :<15s -> texto de 15 caracteres, alineado a la izquierda
    #    - :>7.2f -> numero flotante de 7 caracteres, alineado a la derecha, con 2 decimales
    print(f"{numero_item:02d}  | {producto_actual:<15s} | ${precio_actual:>7.2f}")
# 4. Impresion del Pie del Recibo
print("-------------------------------")
print(f"TOTAL:                  ${total:>7.2f}")

