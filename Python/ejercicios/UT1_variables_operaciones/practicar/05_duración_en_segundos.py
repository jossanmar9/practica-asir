# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 05
# Título: Duración en segundos
#
# Pide minutos y segundos y expresa el total en segundos.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

minutos = int(input("Escribe los minutos: "))
segundos = int(input("Escribe los segundos: "))

conversion = minutos * 60
totales = conversion + segundos

print(f"El total de segundos que hay en {minutos} minutos y {segundos} segundos es {totales} segundos")