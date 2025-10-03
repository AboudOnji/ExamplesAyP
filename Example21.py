# Ejercicio 21: Selección de cursos y métodos de pago
# Paso 1: Bienvenida y presentación de los cursos
# Se imprime un mensaje inicial y se listan las opciones para que el usuario sepa qué elegir.
print("¡Bienvenido al instituto de programación!")
print("Estos son nuestros cursos de verano disponibles:")
print("-------------------------------------------------")
print("1. Python para principiantes | Costo: $10,000.00")
print("2. Python intermedio         | Costo: $15,000.00")
print("3. Python avanzado           | Costo: $20,000.00")
print("-------------------------------------------------")

# Paso 2: Preguntar al usuario qué curso desea
# Usamos input() para capturar la elección del usuario. La respuesta se guarda como texto.
opcion_curso = input("Por favor, escribe el número del curso que quieres elegir (1, 2, o 3): ")


# Paso 3: Determinar el costo base según el curso elegido
# Se usa una estructura if-elif-else para evaluar la opción del usuario.
# Comparamos el texto introducido ('1', '2', o '3') para asignar el costo y nombre correctos.
if opcion_curso == '1':
    costo_base = 10000.00
    nombre_curso = "Python para principiantes"
elif opcion_curso == '2':
    costo_base = 15000.00
    nombre_curso = "Python intermedio"
elif opcion_curso == '3':
    costo_base = 20000.00
    nombre_curso = "Python avanzado"
else:
    # Si el usuario escribe algo diferente, se muestra un error y se cambia la bandera a False.
    print("Error: La opción de curso que elegiste no es válida.")
    costo_base = 00.00
    nombre_curso = "Curso no válido"
# Paso 4: Si el curso fue válido, preguntar por el método de pago
print(f"Has elegido el curso: '{nombre_curso}'")
print(f"El costo base es de: ${costo_base:,.2f}")
    
    # Presentar opciones de pago
print("\n--- Formas de pago ---")
print("1. Tarjeta de débito (Sin cargos extra)")
print("2. Tarjeta de crédito (Se aplica un cargo del 7% adicional)")
    
opcion_pago = input("Por favor, elige tu método de pago (1 o 2): ")

if opcion_pago == '1':
    costo_total = costo_base
    print("\n--- Resumen de tu Compra ---")
    print(f"Curso: {nombre_curso}")
    print("Método de pago: Tarjeta de débito")
    print("--------------------------------")
    print(f"Total a pagar: ${costo_total:,.2f}")
        
elif opcion_pago == '2':
    cargo_extra = costo_base * 0.07
    costo_total = costo_base + cargo_extra
    print("\n--- Resumen de tu Compra ---")
    print(f"Curso: {nombre_curso}")
    print("Método de pago: Tarjeta de crédito")
    print("--------------------------------")
    print(f"Costo base:           ${costo_base:,.2f}")
    print(f"Cargo por T.C. (7%):  +${cargo_extra:,.2f}")
    print(f"Total a pagar:        =${costo_total:,.2f}")
        
else:
    print("Error: El método de pago seleccionado no es válido.")