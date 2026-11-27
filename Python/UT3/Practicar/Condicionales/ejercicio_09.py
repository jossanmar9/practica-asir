# Ejercicio 9
#
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

# Escribe tu solución debajo:

numero_1 = float(input("Numero 1: "))
numero_2 = float(input("Numero 2: "))
numero_3 = float(input("Numero 3: "))

if numero_1 >= numero_2 >= numero_3:
    print(numero_1, numero_2, numero_3)

elif numero_1 >= numero_3 >= numero_2:
    print(numero_1, numero_3, numero_2)

elif numero_2 >= numero_1 >= numero_3:
    print(numero_2, numero_1, numero_3)

elif numero_2 >= numero_3 >= numero_1:
    print(numero_2, numero_3, numero_1)

elif numero_3 >= numero_1 >= numero_2:
    print(numero_3, numero_1, numero_2)

else:
    print(numero_3, numero_2, numero_1)