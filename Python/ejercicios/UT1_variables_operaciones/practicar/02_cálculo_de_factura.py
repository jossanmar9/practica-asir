# ENUNCIADO — UT1: variables, tipos, operaciones, entrada y salida
# Modalidad: PRACTICAR | Ejercicio 02
# Título: Cálculo de factura
#
# Pide precio unitario y cantidad; calcula subtotal y un IVA del 12%.
#
# REQUISITOS:
# - Muestra resultados con etiquetas y unidades. Usa variables descriptivas. Prueba un caso normal y uno límite.
# - Usa los conceptos de esta unidad, sin soluciones avanzadas innecesarias.
# - No uses datos personales reales ni modifiques ficheros del sistema.
# - Comprueba que el programa se ejecuta en VS Code o con python3.
#
# ESCRIBE TU SOLUCIÓN A PARTIR DE AQUÍ:

precio = float(input("Introduce el precio unitario: "))
cantidad = int(input("Introduce la canitdad comprada: "))

subtotal = precio * cantidad

IVA = subtotal * 0.21

total = subtotal + IVA

print(f"El subtotal de {cantidad} unidades con un precio de {precio} € es {subtotal:.2f} € y el IVA es {IVA:.2f} €, en total son {total:.2f} €")