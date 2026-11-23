# Simulacro IAW 01

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Recorrido de una petición
Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1 — Archivo estático
Un usuario solicita /manual.pdf desde la carpeta app. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1 — Puerto publicado
En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8081.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT2 — GET y POST
El formulario de presupuesto utiliza method=post y PHP comprueba REQUEST_METHOD. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué sucede en la primera visita GET.

b) (0,40) Indica qué cambiarías si el formulario enviara GET por error.

c) (0,30) Explica cómo verificarías el envío.

## UT2 — Atributo name
El campo correo tiene id=correo pero se elimina name=correo. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué recibirá PHP.

b) (0,40) Indica la corrección mínima.

c) (0,30) Explica qué mensaje de validación aparecería.

## UT2 — Correo inválido
Se introduce una cadena sin formato de correo. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace FILTER_VALIDATE_EMAIL.

b) (0,40) Indica qué bloque impide calcular el presupuesto.

c) (0,30) Explica qué debería conservar el formulario tras el error.
