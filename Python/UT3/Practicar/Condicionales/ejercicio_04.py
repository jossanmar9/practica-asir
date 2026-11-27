# Ejercicio 4
#
# Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

# Escribe tu solución debajo:

numero_1 = int(input("Introduce el primer numero: "))
numero_2 = int(input("Introduce el segundo numero: "))

if numero_2 != 0:
    print(numero_2 / 2)
else:
    print("No se puede dividir entre 0")