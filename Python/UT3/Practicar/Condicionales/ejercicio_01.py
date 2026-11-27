# Ejercicio 1
#
# Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.

# Escribe tu solución debajo:

numero_1 = int(input("Introduce el primer numero: "))
numero_2 = int(input("Introduce el segundo numero: "))

if numero_1 > numero_2:
    print(f"{numero_1} es mayor que {numero_2}")
elif numero_1 < numero_2:
    print(f"{numero_1} no es mayor que {numero_2}")
else:
    print(f"{numero_1} es igual que {numero_2}")