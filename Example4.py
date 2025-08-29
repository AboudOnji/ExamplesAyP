# Example4.py
# Convierte grados Celsius a Fahrenheit
# Formula: F=(9/5)*C+32
# Asegura que la temperatura no sea menor a -273.15 grados Celsius

C=input('ingresa la temperatura en grados Celsius: ')
C=int(C)
if C < -273.15:
    print("la temperatura no puede ser menor a -273.15 grados Celsius")
else:
    F=(9/5)*C+32
    print(C, 'grados Celsius son', F, 'grados Fahrenheit')

