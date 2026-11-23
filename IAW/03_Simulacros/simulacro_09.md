# Simulacro IAW 09

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Variable ausente
El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1 — Nombre de host
En index.php se cambia DB_HOST de db a localhost. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1 — Persistencia de MariaDB
El servicio db monta db_data:/var/lib/mysql. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT2 — Función de precios
obtenerPrecioPlan devuelve 5, 9 o 15. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la función.

b) (0,40) Indica cómo cambiarías el precio de Profesional a 11.

c) (0,30) Explica una prueba que detecte el cambio.

## UT2 — Login correcto
autenticar.php verifica usuario y contraseña con password_verify. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el flujo hasta panel.php.

b) (0,40) Indica qué datos se guardan en la sesión.

c) (0,30) Explica cómo comprobarías la redirección.

## UT2 — Login incorrecto
Un usuario introduce una contraseña incorrecta. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué ocurre con error_login.

b) (0,40) Indica qué página recibe la redirección.

c) (0,30) Explica cómo evitar mostrar información sensible.
