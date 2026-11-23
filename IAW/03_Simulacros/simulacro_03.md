# Simulacro IAW 03

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Captura de errores
index.php usa try/catch(Throwable $e) y muestra KO. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1 — Dependencias
Nginx depende de php y php depende de db. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1 — Archivo .env.example
El repositorio incluye .env.example con nombres de variables. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.

## UT2 — Límite de notas
panel.php permite hasta 3 notas. Variante: el máximo solicitado es 4 notas.

a) (0,30) Explica dónde se controla el máximo.

b) (0,40) Indica el cambio mínimo para permitir 5.

c) (0,30) Explica qué probarías con 4, 5 y 6 notas.

## UT2 — Contador de accesos
panel.php incrementa accesos en GET salvo tras guardar una nota. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no cuenta el GET tras guardar.

b) (0,40) Indica qué variable de sesión interviene.

c) (0,30) Explica una secuencia de peticiones y su resultado.

## UT2 — Cerrar sesión
logout.php destruye la sesión y redirige. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué información deja de estar disponible.

b) (0,40) Indica qué ocurre al volver a panel.php.

c) (0,30) Explica cómo probarías el cierre.
