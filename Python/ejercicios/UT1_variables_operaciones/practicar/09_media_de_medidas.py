# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 09
# Título: Media de medidas
#
# Pide tres mediciones decimales y muestra su media con dos decimales.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

medicion_1 = float(input("Introduce la primera medición: "))
medicion_2 = float(input("Introduce la segunda medición: "))
medicion_3 = float(input("Introduce la tercera medición: "))

media = (medicion_1 + medicion_2 + medicion_3) / 3

print(f"La media es {media:.2f}")