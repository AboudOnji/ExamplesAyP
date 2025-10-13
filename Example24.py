# Ejemplo24: Combinaciones de Ciclos Anidados en Python
# Imagina que tienes dos listas: una con tipos de plato principal y otra con tipos de bebida. 
# Escribe un programa para generar e imprimir todas las combinaciones posibles de menús que se pueden crear. 
# Utiliza ciclos anidados de for para lograr esto.
# Definimos las dos listas con las que vamos a trabajar.
platos_principales = ["Pasta", "Pizza", "Ensalada"]
bebidas = ["Agua", "Refresco", "Jugo"]

print("--- Combinaciones de Menu Posibles ---")

# En la primera vuelta, 'plato' sera "Pasta".
# En la segunda, 'plato' sera "Pizza", etc.
for plato in platos_principales:
    
    # 3. Ciclo Interno
    # Para cada 'plato' del ciclo externo, este bucle recorrera
    # la lista COMPLETA de bebidas.
    for bebida in bebidas:
        
        # 4. Accion
        # Imprimimos la combinacion del plato actual con la bebida actual.
        print(f"Menú: {plato} con {bebida}")