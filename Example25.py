# Ejemplo 25: Encontrar invitados en comun entre dos eventos usando bucles anidados.
# Definimos las dos listas con los nombres de los invitados.
invitados_evento_A = ["Ana", "Carlos", "Sofia", "Luis"]
invitados_evento_B = ["Sofia", "Pedro", "Ana", "Laura"]

# Creamos una lista vacia para guardar los nombres que encontremos en comun.
invitados_comunes = []

print("Buscando invitados en comun...")

# Recorre cada nombre en la primera lista.
for invitado_A in invitados_evento_A:
    
    # Para cada nombre de la lista A, recorre TODOS los nombres de la lista B.
    for invitado_B in invitados_evento_B:
        
        # Comparamos el invitado actual de la lista A con el de la lista B.
        if invitado_A == invitado_B:
            # Si son iguales, hemos encontrado una coincidencia.
            # Agregamos el nombre a nuestra lista de invitados comunes.
            invitados_comunes.append(invitado_A)
            
# Imprimimos la lista que hemos llenado con las coincidencias.
print("Los invitados en comun son:", invitados_comunes)