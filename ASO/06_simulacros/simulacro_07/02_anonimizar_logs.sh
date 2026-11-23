#!/bin/bash
# ASO · SIMULACRO 07 · EJERCICIO 2 (4 puntos)
# Tiempo orientativo: 25-35 minutos por ejercicio.
# Fichero: 02_anonimizar_logs.sh
#
# ENUNCIADO:
# Recibe un fichero .log existente. Usa sed -E para reemplazar patrones IPv4 de 1 a 3
# cifras por octeto con X.X.X.X y guarda resultado en un fichero nuevo con sufijo .anonimo
# en la misma carpeta. No modifiques el original; muestra ruta y líneas procesadas. La
# regex comprueba formato, no rango 0-255.
#
# COMPROBACIÓN SUGERIDA:
# bash 02_anonimizar_logs.sh ../datos/accesos_sim.log
# bash -n 02_anonimizar_logs.sh
#
# REQUISITOS GENERALES:
# - Controla argumentos ausentes, entradas inválidas y casos límite.
# - Usa los conceptos de UT1/UT2, sin herramientas avanzadas innecesarias.
# - No utilices sudo ni modifiques ficheros del sistema.
# - Prueba un caso normal y otro incorrecto.
#
# TODO: escribe tu solución a partir de aquí.
