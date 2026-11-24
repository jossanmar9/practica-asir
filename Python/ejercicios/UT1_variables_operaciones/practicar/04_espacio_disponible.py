# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 04
# Título: Espacio disponible
#
# Pide capacidad total y espacio usado en GB; calcula espacio libre y porcentaje ocupado.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

total = float(input("Escribe la capcidad total en GB del disco:"))
usado = float(input("Escribe el espacio usado en disco: "))

libre = total - usado

porcentaje = (usado * 100) / total

print(f"Els espacio libre del disco es de {libre} GB y el porcentaje usado de {porcentaje:.2f}%")