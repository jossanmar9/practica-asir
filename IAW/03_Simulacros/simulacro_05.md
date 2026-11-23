# Simulacro IAW 05

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Montaje compartido
Nginx y PHP montan ./app:/var/www/html. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1 — Dockerfile PHP
El servicio PHP se construye desde ./php. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1 — Consulta de prueba
index.php hace SELECT COUNT(*) FROM prueba. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT2 — Plan nuevo
Se quiere añadir un plan Premium de 12 euros al mes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica dónde se valida el plan actualmente.

b) (0,40) Indica todos los bloques que habría que actualizar.

c) (0,30) Explica cómo probarías el cálculo y la selección.

## UT2 — Precio de extras
Backup cuesta 2 euros/mes y soporte 3 euros/mes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Calcula el extra mensual con ambos marcados.

b) (0,40) Indica qué cambiarías si backup costara 4 euros.

c) (0,30) Explica una prueba con 6 meses.

## UT2 — Checkbox ausente
Un usuario no marca soporte. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué puede faltar $_POST[soporte].

b) (0,40) Indica cómo lo trata isset.

c) (0,30) Explica cómo probarías ambos estados.
