# Ejemplo 23: Tablas de multiplicar del 1 al 10 usando bucles anidados
# Ciclo externo para controlar el numero de la tabla (del 1 al 10)
for tabla in range(1, 11):
  
    # Imprime un encabezado para cada nueva tabla, con un salto de linea antes
    print(f"\n--- Tabla del {tabla} ---")
    
    # Ciclo interno para controlar el multiplicador (del 1 al 10)
    # Este ciclo se ejecuta 10 veces por CADA numero de tabla
    for multiplicador in range(1, 11):
      
        # Calcula el resultado de la multiplicacion
        resultado = tabla * multiplicador
        
        # Imprime la linea de la tabla con un formato claro
        print(f"{tabla} x {multiplicador} = {resultado}")