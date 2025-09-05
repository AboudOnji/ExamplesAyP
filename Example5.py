# Example5.py
# Crea una contraseña segura
# La contraseña debe tener al menos 8 caracteres
# Si la contraseña es inválida, pide al usuario que intente de nuevo
# Si la contraseña es válida, muestra un mensaje de éxito y termina

contrasena_valida = False
while not contrasena_valida:
    contrasena = input("Cree una contraseña (mínimo 8 caracteres): ")
    if len(contrasena) >= 8:
        contrasena_valida = True
        print("¡Contraseña creada exitosamente!")
    else:
        print("Error: La contraseña es demasiado corta. Inténtelo de nuevo.\n")

#FIN del algoritmo.