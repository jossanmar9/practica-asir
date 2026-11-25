# Ejercicio 13
#
# Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Utiliza potencias para ello.

# Escribe tu solución debajo:

numero = int(input("Escribe un número: "))

cuadrada = numero ** 0.5
cubica = numero ** (1/3)

print("La raiz cuadrada es", round(cuadrada, 2), "y la cubica", round(cubica, 2))