# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 12
# Título: Intercambiar variables
#
# Pide dos valores y muestra ambos antes y después de intercambiarlos.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

variable_1 = input("Escribe un valor: ")
variable_2 = input("Escribe un valor: ")

print(variable_1)
print(variable_2)

variable_3 = variable_2
variable_2 = variable_1
variable_1 = variable_3

print(variable_1)
print(variable_2)