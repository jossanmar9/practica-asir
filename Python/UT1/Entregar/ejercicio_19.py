# Ejercicio 19
#
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

# Escribe tu solución debajo:

correcta = int(input("Escribe el numero de respuestas correctas: "))
incorrecta = int(input("Escribe el numero de respuestas incorrectas: "))
blanco = int(input("Escribe el numero de respuestas en blanco: "))

puntos = (correcta * 5) + (incorrecta * -1)

print("El resultado es: ", puntos)