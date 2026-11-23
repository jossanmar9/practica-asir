#!/bin/bash
# ASO · SIMULACRO 10 · EJERCICIO 1 (4 puntos)
# Tiempo orientativo: 25-35 minutos por ejercicio.
# Fichero: 01_gestion_usuarios_simulada.sh
#
# ENUNCIADO:
# Recibe acción alta o baja con case. Alta: solicita login con read, valida regex
# ^[a-z][a-z0-9]*$, comprueba existencia con id y muestra (sin ejecutar) comando useradd.
# Baja: recibe login como segundo parámetro, valida formato y existencia y muestra (sin
# ejecutar) userdel. Usa funciones y mensajes de error.
#
# COMPROBACIÓN SUGERIDA:
# bash 01_gestion_usuarios_simulada.sh alta
# bash -n 01_gestion_usuarios_simulada.sh
#
# REQUISITOS GENERALES:
# - Controla argumentos ausentes, entradas inválidas y casos límite.
# - Usa los conceptos de UT1/UT2, sin herramientas avanzadas innecesarias.
# - No utilices sudo ni modifiques ficheros del sistema.
# - Prueba un caso normal y otro incorrecto.
#
# TODO: escribe tu solución a partir de aquí.
