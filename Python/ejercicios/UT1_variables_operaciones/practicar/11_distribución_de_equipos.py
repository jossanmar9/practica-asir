# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 11
# Título: Distribución de equipos
#
# Pide número de equipos y capacidad por armario; calcula armarios completos y equipos sobrantes con // y %.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

equipos = int(input("Quantos equipos hay: "))
armarios = int(input("Cuantos equipos caben en cada armario: "))

capacidad = equipos // armarios
sobrante = equipos % armarios

print("Caben", capacidad, "equipos en los armarios y sobra", sobrante, "equipos")

