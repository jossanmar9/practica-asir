#!/bin/bash
# ASO · SIMULACRO 06 · EJERCICIO 1 (4 puntos)
# Tiempo orientativo: 25-35 minutos por ejercicio.
# Fichero: 01_inventario_usuarios.sh
#
# ENUNCIADO:
# Lee /etc/passwd con while IFS=: read -r; recibe una shell opcional (por defecto
# /bin/bash) y valida su formato como ruta absoluta con regex. Muestra usuario, UID y home
# de cuentas coincidentes y total con UID >= 1000.
#
# COMPROBACIÓN SUGERIDA:
# bash 01_inventario_usuarios.sh /bin/bash
# bash -n 01_inventario_usuarios.sh
#
# REQUISITOS GENERALES:
# - Controla argumentos ausentes, entradas inválidas y casos límite.
# - Usa los conceptos de UT1/UT2, sin herramientas avanzadas innecesarias.
# - No utilices sudo ni modifiques ficheros del sistema.
# - Prueba un caso normal y otro incorrecto.
#
# TODO: escribe tu solución a partir de aquí.
