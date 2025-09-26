# Ejemplo 18: Recibo de compra con listas y formato profesional
# Este programa genera un recibo de compra formateado profesionalmente
# utilizando listas paralelas para almacenar productos y sus precios.
# El usuario ingresa productos y precios hasta que ingresa un precio de 0.
# -------------------------------------------------------------------------------------

Producto = []
Costo = []
i=0
while True:
    P = input("Cual es el producto que has comprado?")
    C = float(input("Cual es el costo del producto?"))
    if C != 0:
        Producto.append(P)
        Costo.append(C)
    else:
        break
    i+=1
print("--- RECIBO DE COMPRA ---")
print("No. | Producto        | Precio")
print("-------------------------------")
# 3. Bucle para recorrer las listas por indice
# range(len(productos)) genera una secuencia de numeros: 0, 1, 2
total = 0.0
for j in range(len(Producto)):
    
    # a. Acceder a los datos usando el indice 'i'
    numero_item = j + 1
    producto_actual = Producto[j]
    precio_actual = Costo[j]
    
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