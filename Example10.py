# Ejemplo 10: Simulacion de un Cajero Automatico (ATM) con bucle y condicionales
# Este programa permite al usuario consultar su saldo, depositar y retirar dinero
# Usamos un bucle 'while' para mostrar el menu repetidamente hasta que el usuario
# decida salir. Tambien usamos condicionales 'if', 'elif' y 'else' para manejar
# las diferentes opciones del menu.
# 1. Inicializacion
# Empezamos con un saldo inicial de 1000.0
saldo = 1000.0

# 2. Bucle principal del cajero
# Usamos 'while True' para que el menu se repita indefinidamente
while True:
    # 3. Mostrar menu de opciones
    print("\n--- Cajero Automatico (ATM) ---") # \n es un salto de linea
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Retirar Dinero")
    print("4. Salir")
    print("---------------------------------")
    
    # 4. Solicitar la opcion al usuario
    opcion = input("Por favor, seleccione una opcion (1-4): ")
    
    # 5. Logica condicional para cada opcion
    if opcion == '1':
        # Opcion 1: Consultar Saldo
        # Usamos un f-string para formatear la salida a 2 decimales
        print("\n✅ Su saldo actual es: ",saldo)
        
    elif opcion == '2':
        # Opcion 2: Depositar Dinero
        cantidad_str = input("Ingrese la cantidad a depositar: ")
        # Convertimos la entrada (string) a un numero flotante (float)
        cantidad = float(cantidad_str)
        
        # Realizamos la operacion matematica
        saldo = saldo + cantidad # o tambien: saldo += cantidad
        
        print("\n✅ Deposito exitoso, su saldo actual es: ",saldo)
        
    elif opcion == '3':
        # Opcion 3: Retirar Dinero
        cantidad_str = input("Ingrese la cantidad a retirar: ")
        cantidad = float(cantidad_str)
        
        # Verificamos si hay fondos suficientes
        if cantidad <= saldo:
            # Si hay fondos, realizamos la operacion
            saldo = saldo - cantidad # o tambien: saldo -= cantidad
            print("\n✅ Retiro exitosis, su saldo actual es: ",saldo)
        else:
            # Si no hay fondos, mostramos un error
            print("\n Fondo insuficiente. Su saldo actual es: ",saldo)
            
    elif opcion == '4':
        # Opcion 4: Salir
        print("\n👋 Gracias por utilizar el Cajero Automatico. ¡Hasta luego!")
        break # La palabra clave 'break' rompe el bucle y termina el programa
        
    else:
        # Opcion Invalida
        print("\n❌ Error: Opcion no valida. Por favor, intente de nuevo.")