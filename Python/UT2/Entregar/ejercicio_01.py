# Ejercicio 1: Normalizar hostname de aula
#
# Pista: strip y replace
#
# Dado el texto ' pc -- aula - 07 \n' debes convertirlo a 'PC-AULA-07' sin usar condicionales ni bucles. Imprime el resultado.

# Escribe tu solución debajo:

texto = " pc -- aula - 07 \n" 

limpio = texto.strip()
mayusculas = limpio.upper()
espacios = mayusculas.replace(" ", "")
guiones = espacios.replace("--", "-")

print(guiones)