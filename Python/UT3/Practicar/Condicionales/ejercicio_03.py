# Ejercicio 3
#
# Escribe un programa que lea un número e indique si es par o impar.

# Escribe tu solución debajo:

numero = int(input("Escribe un numero: "))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")