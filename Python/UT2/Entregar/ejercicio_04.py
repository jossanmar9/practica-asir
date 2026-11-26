# Ejercicio 4: Analizar y trocear IP v4
#
# Pista: strip, count, find y [:]
#
# Dada la IP ' 192.168.001.010 ': limpia bordes, cuenta puntos, extrae el primer octeto (hasta primer '.') y último octeto (desde último '.'). Imprime estos 2 octetos.

# Escribe tu solución debajo:

direccion = " 192.168.001.010 "

limpia = direccion.strip()

print(limpia.count("."))

primero = limpia.find(".")
segundo = limpia.find(".", primero + 1)
tercero = limpia.find(".", segundo + 1)

print(limpia[:primero])
print(limpia[tercero + 1:])