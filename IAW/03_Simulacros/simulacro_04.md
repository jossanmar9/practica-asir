# Simulacro IAW 04

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Variable ausente
El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1 — Nombre de host
En index.php se cambia DB_HOST de db a localhost. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1 — Persistencia de MariaDB
El servicio db monta db_data:/var/lib/mysql. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT2 — Número entero
El usuario introduce 2.5 meses. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no es válido.

b) (0,40) Identifica la función usada para validarlo.

c) (0,30) Explica qué debería mostrarse en vez de un total.

## UT2 — Sesión tras login
El login llama a session_regenerate_id(true). Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve.

b) (0,40) Indica en qué momento se llama.

c) (0,30) Explica qué debe conservarse en la sesión después.

## UT2 — GET y POST
El formulario de presupuesto utiliza method=post y PHP comprueba REQUEST_METHOD. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué sucede en la primera visita GET.

b) (0,40) Indica qué cambiarías si el formulario enviara GET por error.

c) (0,30) Explica cómo verificarías el envío.
