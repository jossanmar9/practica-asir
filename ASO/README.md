# Prácticas de ASO — Bash y procesos (sin resolver)

Basadas en los temas y las prácticas aportadas para el examen del 1 de diciembre.

## Distribución
- 01_basicos/01_variables: 6 ejercicios
- 01_basicos/02_condicionales: 6 ejercicios
- 01_basicos/03_for: 6 ejercicios
- 01_basicos/04_while: 6 ejercicios
- 01_basicos/05_case: 6 ejercicios (case es una estructura de selección, no un bucle)
- 02_funciones: 6 ejercicios
- 03_regex: 15 ejercicios
- 04_sed: 6 ejercicios
- 05_procesos: 6 ejercicios
- 06_simulacros: 20 ejercicios (10 simulacros de 2 scripts)

**Total: 83 scripts .sh**. Los scripts están sin resolver. Los ejercicios originales de las demás secciones se conservan.

## Cómo practicar
1. Abre un fichero .sh y escribe tu solución bajo el comentario final.
2. Comprueba la sintaxis: `bash -n archivo.sh`.
3. Ejecuta con `bash archivo.sh argumentos` o con `chmod +x archivo.sh` y `./archivo.sh`.
4. Prueba casos normales, incorrectos y límites.

## Seguridad
Los ejercicios de procesos deben probarse de manera no destructiva. No ejecutes `kill`, `renice` ni modificaciones del sistema sin saber exactamente qué proceso o fichero afectas.

## Diez simulacros de examen
Cada simulacro consta de dos ejercicios de 4 puntos (8 puntos prácticos).
- Simulacros 1–3: seis scripts originales de la carpeta 06_simulacros.
- Simulacros 4–10: subcarpetas simulacro_04 a simulacro_10, con dos scripts cada una.
- No incluyen soluciones. Hay ficheros de datos adicionales en datos/.
- Completa la parte teórica (2 puntos) por separado.
