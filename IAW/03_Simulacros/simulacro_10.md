# Simulacro IAW 10

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Montaje compartido
Nginx y PHP montan ./app:/var/www/html. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1 — Dockerfile PHP
El servicio PHP se construye desde ./php. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1 — Consulta de prueba
index.php hace SELECT COUNT(*) FROM prueba. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT2 — Cerrar sesión
logout.php destruye la sesión y redirige. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué información deja de estar disponible.

b) (0,40) Indica qué ocurre al volver a panel.php.

c) (0,30) Explica cómo probarías el cierre.

## UT2 — Redirección PRG
Tras guardar una nota se redirige a panel.php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve POST-Redirect-GET.

b) (0,40) Razona qué pasaría al recargar si no se redirigiera.

c) (0,30) Indica cómo comprobarías que no se duplica la nota.

## UT2 — Sesiones aisladas
Ana y Marcos inician sesión desde navegadores diferentes. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica si comparten notas y contador.

b) (0,40) Indica qué estructura almacena los datos de cada sesión.

c) (0,30) Explica cómo verificarías el aislamiento.
