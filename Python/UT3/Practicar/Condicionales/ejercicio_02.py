# Ejercicio 2
#
# Algoritmo que pida un número y diga si es positivo, negativo o 0.

# Escribe tu solución debajo:

numero = int(input("Escribe un numero: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")