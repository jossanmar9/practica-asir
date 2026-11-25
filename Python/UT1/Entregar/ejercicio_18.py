# Ejercicio 18
#
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

# Escribe tu solución debajo:

nombre = input("Escribe tu nombre: ")
apellido_1 = input("Escribe tu primer apellido: ")
apellido_2 = input("Escribe tu segundo apellido: ")


print(nombre[0:1].upper(), apellido_1[0:1].upper(), apellido_2[0:1].upper(), sep="")