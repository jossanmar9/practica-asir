# Ejercicio 7
#
# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

# Escribe tu solución debajo:

minutos = int(input("Minutos: "))

conversion = minutos // 60
resto = minutos % 60

print(conversion, "horas y", resto, "minutos")