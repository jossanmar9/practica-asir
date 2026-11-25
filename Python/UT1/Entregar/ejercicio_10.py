# Ejercicio 10
#
# Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#
#     55% del promedio de sus tres calificaciones parciales.
#     30% de la calificación del examen final.
#     15% de la calificación de un trabajo final.

# Escribe tu solución debajo:

parcial_1 = float(input("Parcial 1: "))
parcial_2 = float(input("Parcial 2: "))
parcial_3 = float(input("Parcial 3: "))
examen = float(input("Examen: "))
trabajo = float(input("Trabajo: "))

promedio = (parcial_1 + parcial_2 + parcial_3) / 3

nota_1 = promedio * 0.55
nota_2 = examen * 0.30
nota_3 = trabajo * 0.15

nota_final = nota_1 + nota_2 + nota_3

print(f"{nota_final:.2f}")