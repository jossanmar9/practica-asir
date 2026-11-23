# Simulacro IAW 07

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Inicialización SQL
Se modifica sql/init.sql pero la tabla existente no cambia. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1 — PHP-FPM inaccesible
Nginx devuelve 502 al solicitar index.php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1 — Archivo Nginx
El archivo nginx/default.conf reenvía .php al servicio php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT2 — Sesiones aisladas
Ana y Marcos inician sesión desde navegadores diferentes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica si comparten notas y contador.

b) (0,40) Indica qué estructura almacena los datos de cada sesión.

c) (0,30) Explica cómo verificarías el aislamiento.

## UT2 — Validación del nombre
El presupuesto recibe un nombre compuesto solo por espacios. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace trim.

b) (0,40) Indica qué validación lo rechaza.

c) (0,30) Explica cómo probarías la respuesta.

## UT2 — Número entero
El usuario introduce 2.5 meses. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no es válido.

b) (0,40) Identifica la función usada para validarlo.

c) (0,30) Explica qué debería mostrarse en vez de un total.
