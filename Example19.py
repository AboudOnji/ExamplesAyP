# Ejercicio 19: Ingresar notas y materias hasta que se ingrese -1
# y luego mostrar las listas de notas y materias ingresadas.

notas = []
materias =[]
while True:
    materia = input("Ingrese nombre de materia")
    nota = float(input("Ingrese una nota (o -1 para terminar):"))
    if nota == -1:
        break
    else:
        notas.append(nota)
        materias.append(materia)
print(f"Materias ingresadas: {materias}")
print(f"Notas ingresadas: {notas}")
    