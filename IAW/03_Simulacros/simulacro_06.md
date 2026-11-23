# Simulacro IAW 06

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Recorrido de una petición
Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1 — Archivo estático
Un usuario solicita /manual.pdf desde la carpeta app. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1 — Puerto publicado
En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8083.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT2 — Login incorrecto
Un usuario introduce una contraseña incorrecta. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué ocurre con error_login.

b) (0,40) Indica qué página recibe la redirección.

c) (0,30) Explica cómo evitar mostrar información sensible.

## UT2 — Protección del panel
Un visitante abre panel.php sin sesión autenticada. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la comprobación inicial.

b) (0,40) Indica qué cambiarías para proteger otra página privada.

c) (0,30) Explica cómo comprobarías que no se puede entrar.

## UT2 — Límite de notas
panel.php permite hasta 3 notas. Variante: el máximo solicitado es 5 notas.

a) (0,30) Explica dónde se controla el máximo.

b) (0,40) Indica el cambio mínimo para permitir 5.

c) (0,30) Explica qué probarías con 4, 5 y 6 notas.
