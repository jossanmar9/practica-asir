# Ejercicio 3
#
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

# Escribe tu solución debajo:

cateto_1 = float(input("Cateto 1: "))
cateto_2 = float(input("Cateto 2: "))

hipotenusa = ((cateto_1 ** 2) + (cateto_2 ** 2)) ** 0.5

print("La hipotenusa del triangulo formada por los catetos", cateto_1, "y", cateto_2, "es", round(hipotenusa, 2))