# Simulacro IAW 02

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Inicialización SQL
Se modifica sql/init.sql pero la tabla existente no cambia. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1 — PHP-FPM inaccesible
Nginx devuelve 502 al solicitar index.php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1 — Archivo Nginx
El archivo nginx/default.conf reenvía .php al servicio php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT2 — Checkbox ausente
Un usuario no marca soporte. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué puede faltar $_POST[soporte].

b) (0,40) Indica cómo lo trata isset.

c) (0,30) Explica cómo probarías ambos estados.

## UT2 — Escapar HTML
El nombre del presupuesto se muestra con htmlspecialchars. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué riesgo reduce.

b) (0,40) Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML.

c) (0,30) Explica dónde más debe escaparse la salida.

## UT2 — Función de precios
obtenerPrecioPlan devuelve 5, 9 o 15. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la función.

b) (0,40) Indica cómo cambiarías el precio de Profesional a 11.

c) (0,30) Explica una prueba que detecte el cambio.
