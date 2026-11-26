# Ejercicio 3: Partes de una ruta Windows
#
# Pista: find o index y [:]
#
# Dada una ruta como 'C:\\Users\\alumno\\Desktop\\proyecto', extrae: unidad 'C', usuario 'alumno' y carpeta 'Desktop' usando find/index y [:]. Imprime cada uno de los valores.

# Escribe tu solución debajo:

ruta = "C:\\Users\\alumno\\Desktop\\proyecto"

primero = ruta.find("\\")
segundo = ruta.find("\\", primero + 1)
tercero = ruta.find("\\", segundo + 1)
cuarto = ruta.find("\\", tercero + 1)

print(ruta[0:primero - 1])
print(ruta[segundo + 1:tercero])
print(ruta[tercero +1:cuarto])