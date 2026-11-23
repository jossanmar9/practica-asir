#!/bin/bash
# ASO · SIMULACRO 10 · EJERCICIO 2 (4 puntos)
# Tiempo orientativo: 25-35 minutos por ejercicio.
# Fichero: 02_gestion_procesos_segura.sh
#
# ENUNCIADO:
# Menú while/case: 1) listar procesos por usuario; 2) consultar PID; 3) mostrar comando de
# renice que correspondería a un PID y nice entre -20 y 19; 4) mostrar comando SIGTERM que
# correspondería a un PID; 5) salir. Valida PID con regex y ps -p. IMPORTANTE: no ejecutes
# renice ni kill; solo imprime los comandos.
#
# COMPROBACIÓN SUGERIDA:
# bash 02_gestion_procesos_segura.sh 
# bash -n 02_gestion_procesos_segura.sh
#
# REQUISITOS GENERALES:
# - Controla argumentos ausentes, entradas inválidas y casos límite.
# - Usa los conceptos de UT1/UT2, sin herramientas avanzadas innecesarias.
# - No utilices sudo ni modifiques ficheros del sistema.
# - Prueba un caso normal y otro incorrecto.
#
# TODO: escribe tu solución a partir de aquí.
