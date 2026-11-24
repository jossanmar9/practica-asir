# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 10
# Título: Segundos de servicio
#
# Pide horas, minutos y segundos y calcula duración total en segundos.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

horas = int(input("Esribe las horas: "))
minutos = int(input("Introduce los minutos: "))
segundos = int(input("Introduce los segundos: "))

minutos_t = horas * 60
segundos_t = (minutos + minutos_t) * 60
segundos_t = segundos + segundos_t

print(f"Los segundos totales que hay en {horas} horas, {minutos} minutos y {segundos} segundos es {segundos_t} segundos")