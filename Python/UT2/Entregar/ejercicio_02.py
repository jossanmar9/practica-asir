# Ejercicio 2: Prefijo y extracción de aula y número
#
# Pista: startswith, find y [:]
#
# Dada la etiqueta 'PC-AULA-23', verifica si empieza por 'PC-' (solo muestra True o False) y extrae 'AULA' y '23' usando find y [:] (troceado de cadenas). No uses condicionales; solo imprime las partes obtenidas.

# Escribe tu solución debajo:

etiqueta = "PC-DESPACHO-123"

print(etiqueta.startswith("PC-"))

primero = etiqueta.find("-")
segundo = etiqueta.find("-", primero + 1)

print(etiqueta[primero + 1:segundo])
print(etiqueta[segundo + 1:])
