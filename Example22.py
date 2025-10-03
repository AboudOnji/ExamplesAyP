# Ejercicio 22: Clasificación de autos por año y días de no circulación
# Escribe un programa que permita a los usuarios ingresar el año de varios autos.
# El programa debe clasificar cada auto en uno de cuatro grupos según su año.
# Paso 1: Inicializar los contadores para cada grupo
# Estas variables guardarán la cantidad de autos en cada categoría. Empiezan en 0.
contador_grupo_a = 0
contador_grupo_b = 0
contador_grupo_c = 0
contador_grupo_d = 0

# Paso 2: Mostrar la tabla de criterios al usuario
# Es una buena práctica mostrar las reglas del programa primero.
print("--- Sistema de Verificación Vehicular ---")
print("El programa clasifica los autos según su año y determina sus días de no circulación:")
print("---------------------------------------------------------------------")
print("- (Grupo A) 2021 a 2025: Circula todos los días.")
print("- (Grupo B) 2011 a 2020: Deja de circular 1 día al mes.")
print("- (Grupo C) 2006 a 2010: Deja de circular 1 día a la semana.")
print("- (Grupo D) 2000 a 2005: Deja de circular 2 días a la semana.")
print("---------------------------------------------------------------------")

# Paso 3: Preguntar al usuario cuántos autos va a evaluar
# Usamos int(input(...)) para convertir la respuesta del usuario de texto a un número entero.
num_autos = int(input("\n¿Cuántos autos deseas evaluar? "))

# Paso 4: Iniciar el bucle FOR
# El bucle se repetirá el número de veces que el usuario especificó.
# Usamos i + 1 para que el mensaje sea "Auto #1", "Auto #2", etc.
for i in range(num_autos):
    print(f"\n--- Evaluando Auto  ---")
    # Paso 5: Solicitar el año del auto actual
    año = int(input(f"Introduce el año del modelo del auto"))
    
    # Paso 6: Utilizar IF-ELIF-ELSE para evaluar el año y actualizar contadores
    # Se evalúa cada condición en orden. Cuando una es verdadera, se ejecuta su código y se salta el resto.
    if año >= 2021 and año <= 2025:
        print(f"Resultado: El auto año {año} pertenece al Grupo A. Circula todos los días.")
        contador_grupo_a += 1 # Incrementa el contador del grupo A en 1
        
    elif año >= 2011 and año <= 2020:
        print(f"Resultado: El auto año {año} pertenece al Grupo B. Deja de circular 1 día al mes.")
        contador_grupo_b += 1 # Incrementa el contador del grupo B en 1
        
    elif año >= 2006 and año <= 2010:
        print(f"Resultado: El auto año {año} pertenece al Grupo C. Deja de circular 1 día a la semana.")
        contador_grupo_c += 1 # Incrementa el contador del grupo C en 1
        
    elif año >= 2000 and año <= 2005:
        print(f"Resultado: El auto año {año} pertenece al Grupo D. Deja de circular 2 días a la semana.")
        contador_grupo_d += 1 # Incrementa el contador del grupo D en 1
        
    else:
        # Este bloque se ejecuta si ninguna de las condiciones anteriores fue verdadera.
        print(f"Resultado: El auto año {año} está fuera del rango de evaluación (2000-2025).")

# Paso 7: Mostrar el resumen final cuando el bucle termine
print("\n==============================================")
print("--- Resumen Final de la Evaluación ---")
print("==============================================")
print(f"Total de autos en Grupo A: {contador_grupo_a}")
print(f"Total de autos en Grupo B: {contador_grupo_b}")
print(f"Total de autos en Grupo C: {contador_grupo_c}")
print(f"Total de autos en Grupo D: {contador_grupo_d}")
print("==============================================")