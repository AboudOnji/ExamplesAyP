# Ejemplo 11: Sistema de Acceso a una Montana Rusa con Reglas Logicas
# Este programa determina si una persona puede subir a una montana rusa
# basada en su edad, altura y si tiene un pase V.I.P.
# Reglas:
# 1. La persona debe tener mas de 1.40 metros de altura.
# 2. La persona debe tener entre 10 y 60 años de edad (inclusive).
# 3. Excepcion: Si la persona tiene un pase V.I.P., puede subir
#    aunque no cumpla la regla de edad, siempre y cuando tenga al menos 7 años.
# 4. La persona no puede subir si tiene menos de 7 años, incluso con pase V.I.P.
# --- 1. Recopilacion y Conversion de Datos ---

print("--- Sistema de Acceso a la Montana Rusa ---")

# Pedimos la edad y la convertimos a entero (int)
edad = int(input("Ingrese su edad: "))

# Pedimos la altura y la convertimos a flotante (float)
altura = float(input("Ingrese su altura en metros (ej: 1.75): "))

# Pedimos el pase, lo convertimos a minusculas y lo comparamos para obtener un booleano
respuesta_pase = input("¿Tiene pase V.I.P.? (Sí/No): ")
tiene_pase_vip = respuesta_pase.lower() == 'sí'


# --- 2. Implementacion de las Reglas Logicas ---

# Definimos la regla principal en una variable booleana para mayor claridad
regla_principal = (altura > 1.40) and (10 <= edad <= 60)

# Definimos la regla de excepcion en otra variable booleana
# NOT (edad < 7) es lo mismo que (edad >= 7)
regla_excepcion = tiene_pase_vip and (edad >= 7)


# --- 3. Decision Final con el Operador OR ---

# La persona puede subir si cumple la regla principal O la regla de excepcion.
if regla_principal or regla_excepcion:
    # Si cualquiera de las dos condiciones es True, se concede el acceso.
    print("\n Acceso Concedido. ¡Disfrute la atracción!")
else:
    # Si ambas condiciones son False, se deniega el acceso.
    print("\n Acceso Denegado. No cumple con los requisitos de seguridad.")