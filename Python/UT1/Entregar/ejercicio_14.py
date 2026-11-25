# Ejercicio 14
#
# Dado un número entero de dos cifras, diseñe un algoritmo que permita obtener el número invertido utilizando operaciones aritméticas. Ejemplo, si se introduce 23 que muestre 32.

# Escribe tu solución debajo:

numero = int(input("Introduce un numero de 2 cirfas: "))

decena = numero // 10
unidad = numero % 10

inverso = (unidad * 10) + decena

print(inverso)