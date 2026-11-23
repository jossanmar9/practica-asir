#!/bin/bash
# ASO · SIMULACRO 09 · EJERCICIO 1 (4 puntos)
# Tiempo orientativo: 25-35 minutos por ejercicio.
# Fichero: 01_clasificar_http.sh
#
# ENUNCIADO:
# Recibe fichero con códigos HTTP, uno por línea. Usa función clasificar_http con if/elif:
# 200-299 éxito, 300-399 redirección, 400-499 error cliente, 500-599 error servidor, otros
# no clasificados. Valida cada línea con regex y muestra totales.
#
# COMPROBACIÓN SUGERIDA:
# bash 01_clasificar_http.sh ../datos/http_sim.txt
# bash -n 01_clasificar_http.sh
#
# REQUISITOS GENERALES:
# - Controla argumentos ausentes, entradas inválidas y casos límite.
# - Usa los conceptos de UT1/UT2, sin herramientas avanzadas innecesarias.
# - No utilices sudo ni modifiques ficheros del sistema.
# - Prueba un caso normal y otro incorrecto.
#
# TODO: escribe tu solución a partir de aquí.
