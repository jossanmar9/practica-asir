# UT2 — 60 casos de interpretación y modificación

Cada caso vale 1 punto: a) 0,30; b) 0,40; c) 0,30. Responde por escrito y justifica cómo comprobarías el cambio.

## UT2-001 — GET y POST

El formulario de presupuesto utiliza method=post y PHP comprueba REQUEST_METHOD. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué sucede en la primera visita GET.

b) (0,40) Indica qué cambiarías si el formulario enviara GET por error.

c) (0,30) Explica cómo verificarías el envío.

## UT2-002 — Atributo name

El campo correo tiene id=correo pero se elimina name=correo. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué recibirá PHP.

b) (0,40) Indica la corrección mínima.

c) (0,30) Explica qué mensaje de validación aparecería.

## UT2-003 — Correo inválido

Se introduce una cadena sin formato de correo. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace FILTER_VALIDATE_EMAIL.

b) (0,40) Indica qué bloque impide calcular el presupuesto.

c) (0,30) Explica qué debería conservar el formulario tras el error.

## UT2-004 — Límite de meses

El presupuesto admite de 1 a 24 meses. Variante: el nuevo límite solicitado es 25 meses.

a) (0,30) Explica qué ocurre con 25 meses.

b) (0,40) Indica los cambios necesarios para admitir hasta 36.

c) (0,30) Explica qué casos probarías.

## UT2-005 — Plan nuevo

Se quiere añadir un plan Premium de 12 euros al mes. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica dónde se valida el plan actualmente.

b) (0,40) Indica todos los bloques que habría que actualizar.

c) (0,30) Explica cómo probarías el cálculo y la selección.

## UT2-006 — Precio de extras

Backup cuesta 2 euros/mes y soporte 3 euros/mes. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Calcula el extra mensual con ambos marcados.

b) (0,40) Indica qué cambiarías si backup costara 4 euros.

c) (0,30) Explica una prueba con 6 meses.

## UT2-007 — Checkbox ausente

Un usuario no marca soporte. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué puede faltar $_POST[soporte].

b) (0,40) Indica cómo lo trata isset.

c) (0,30) Explica cómo probarías ambos estados.

## UT2-008 — Escapar HTML

El nombre del presupuesto se muestra con htmlspecialchars. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué riesgo reduce.

b) (0,40) Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML.

c) (0,30) Explica dónde más debe escaparse la salida.

## UT2-009 — Función de precios

obtenerPrecioPlan devuelve 5, 9 o 15. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la función.

b) (0,40) Indica cómo cambiarías el precio de Profesional a 11.

c) (0,30) Explica una prueba que detecte el cambio.

## UT2-010 — Login correcto

autenticar.php verifica usuario y contraseña con password_verify. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el flujo hasta panel.php.

b) (0,40) Indica qué datos se guardan en la sesión.

c) (0,30) Explica cómo comprobarías la redirección.

## UT2-011 — Login incorrecto

Un usuario introduce una contraseña incorrecta. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué ocurre con error_login.

b) (0,40) Indica qué página recibe la redirección.

c) (0,30) Explica cómo evitar mostrar información sensible.

## UT2-012 — Protección del panel

Un visitante abre panel.php sin sesión autenticada. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la comprobación inicial.

b) (0,40) Indica qué cambiarías para proteger otra página privada.

c) (0,30) Explica cómo comprobarías que no se puede entrar.

## UT2-013 — Límite de notas

panel.php permite hasta 3 notas. Variante: el máximo solicitado es 4 notas.

a) (0,30) Explica dónde se controla el máximo.

b) (0,40) Indica el cambio mínimo para permitir 5.

c) (0,30) Explica qué probarías con 4, 5 y 6 notas.

## UT2-014 — Contador de accesos

panel.php incrementa accesos en GET salvo tras guardar una nota. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no cuenta el GET tras guardar.

b) (0,40) Indica qué variable de sesión interviene.

c) (0,30) Explica una secuencia de peticiones y su resultado.

## UT2-015 — Cerrar sesión

logout.php destruye la sesión y redirige. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué información deja de estar disponible.

b) (0,40) Indica qué ocurre al volver a panel.php.

c) (0,30) Explica cómo probarías el cierre.

## UT2-016 — Redirección PRG

Tras guardar una nota se redirige a panel.php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve POST-Redirect-GET.

b) (0,40) Razona qué pasaría al recargar si no se redirigiera.

c) (0,30) Indica cómo comprobarías que no se duplica la nota.

## UT2-017 — Sesiones aisladas

Ana y Marcos inician sesión desde navegadores diferentes. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica si comparten notas y contador.

b) (0,40) Indica qué estructura almacena los datos de cada sesión.

c) (0,30) Explica cómo verificarías el aislamiento.

## UT2-018 — Validación del nombre

El presupuesto recibe un nombre compuesto solo por espacios. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace trim.

b) (0,40) Indica qué validación lo rechaza.

c) (0,30) Explica cómo probarías la respuesta.

## UT2-019 — Número entero

El usuario introduce 2.5 meses. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no es válido.

b) (0,40) Identifica la función usada para validarlo.

c) (0,30) Explica qué debería mostrarse en vez de un total.

## UT2-020 — Sesión tras login

El login llama a session_regenerate_id(true). Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve.

b) (0,40) Indica en qué momento se llama.

c) (0,30) Explica qué debe conservarse en la sesión después.

## UT2-021 — GET y POST

El formulario de presupuesto utiliza method=post y PHP comprueba REQUEST_METHOD. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué sucede en la primera visita GET.

b) (0,40) Indica qué cambiarías si el formulario enviara GET por error.

c) (0,30) Explica cómo verificarías el envío.

## UT2-022 — Atributo name

El campo correo tiene id=correo pero se elimina name=correo. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué recibirá PHP.

b) (0,40) Indica la corrección mínima.

c) (0,30) Explica qué mensaje de validación aparecería.

## UT2-023 — Correo inválido

Se introduce una cadena sin formato de correo. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace FILTER_VALIDATE_EMAIL.

b) (0,40) Indica qué bloque impide calcular el presupuesto.

c) (0,30) Explica qué debería conservar el formulario tras el error.

## UT2-024 — Límite de meses

El presupuesto admite de 1 a 24 meses. Variante: el nuevo límite solicitado es 26 meses.

a) (0,30) Explica qué ocurre con 25 meses.

b) (0,40) Indica los cambios necesarios para admitir hasta 36.

c) (0,30) Explica qué casos probarías.

## UT2-025 — Plan nuevo

Se quiere añadir un plan Premium de 12 euros al mes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica dónde se valida el plan actualmente.

b) (0,40) Indica todos los bloques que habría que actualizar.

c) (0,30) Explica cómo probarías el cálculo y la selección.

## UT2-026 — Precio de extras

Backup cuesta 2 euros/mes y soporte 3 euros/mes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Calcula el extra mensual con ambos marcados.

b) (0,40) Indica qué cambiarías si backup costara 4 euros.

c) (0,30) Explica una prueba con 6 meses.

## UT2-027 — Checkbox ausente

Un usuario no marca soporte. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué puede faltar $_POST[soporte].

b) (0,40) Indica cómo lo trata isset.

c) (0,30) Explica cómo probarías ambos estados.

## UT2-028 — Escapar HTML

El nombre del presupuesto se muestra con htmlspecialchars. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué riesgo reduce.

b) (0,40) Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML.

c) (0,30) Explica dónde más debe escaparse la salida.

## UT2-029 — Función de precios

obtenerPrecioPlan devuelve 5, 9 o 15. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la función.

b) (0,40) Indica cómo cambiarías el precio de Profesional a 11.

c) (0,30) Explica una prueba que detecte el cambio.

## UT2-030 — Login correcto

autenticar.php verifica usuario y contraseña con password_verify. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el flujo hasta panel.php.

b) (0,40) Indica qué datos se guardan en la sesión.

c) (0,30) Explica cómo comprobarías la redirección.

## UT2-031 — Login incorrecto

Un usuario introduce una contraseña incorrecta. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué ocurre con error_login.

b) (0,40) Indica qué página recibe la redirección.

c) (0,30) Explica cómo evitar mostrar información sensible.

## UT2-032 — Protección del panel

Un visitante abre panel.php sin sesión autenticada. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la comprobación inicial.

b) (0,40) Indica qué cambiarías para proteger otra página privada.

c) (0,30) Explica cómo comprobarías que no se puede entrar.

## UT2-033 — Límite de notas

panel.php permite hasta 3 notas. Variante: el máximo solicitado es 5 notas.

a) (0,30) Explica dónde se controla el máximo.

b) (0,40) Indica el cambio mínimo para permitir 5.

c) (0,30) Explica qué probarías con 4, 5 y 6 notas.

## UT2-034 — Contador de accesos

panel.php incrementa accesos en GET salvo tras guardar una nota. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no cuenta el GET tras guardar.

b) (0,40) Indica qué variable de sesión interviene.

c) (0,30) Explica una secuencia de peticiones y su resultado.

## UT2-035 — Cerrar sesión

logout.php destruye la sesión y redirige. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué información deja de estar disponible.

b) (0,40) Indica qué ocurre al volver a panel.php.

c) (0,30) Explica cómo probarías el cierre.

## UT2-036 — Redirección PRG

Tras guardar una nota se redirige a panel.php. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve POST-Redirect-GET.

b) (0,40) Razona qué pasaría al recargar si no se redirigiera.

c) (0,30) Indica cómo comprobarías que no se duplica la nota.

## UT2-037 — Sesiones aisladas

Ana y Marcos inician sesión desde navegadores diferentes. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica si comparten notas y contador.

b) (0,40) Indica qué estructura almacena los datos de cada sesión.

c) (0,30) Explica cómo verificarías el aislamiento.

## UT2-038 — Validación del nombre

El presupuesto recibe un nombre compuesto solo por espacios. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace trim.

b) (0,40) Indica qué validación lo rechaza.

c) (0,30) Explica cómo probarías la respuesta.

## UT2-039 — Número entero

El usuario introduce 2.5 meses. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no es válido.

b) (0,40) Identifica la función usada para validarlo.

c) (0,30) Explica qué debería mostrarse en vez de un total.

## UT2-040 — Sesión tras login

El login llama a session_regenerate_id(true). Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve.

b) (0,40) Indica en qué momento se llama.

c) (0,30) Explica qué debe conservarse en la sesión después.

## UT2-041 — GET y POST

El formulario de presupuesto utiliza method=post y PHP comprueba REQUEST_METHOD. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué sucede en la primera visita GET.

b) (0,40) Indica qué cambiarías si el formulario enviara GET por error.

c) (0,30) Explica cómo verificarías el envío.

## UT2-042 — Atributo name

El campo correo tiene id=correo pero se elimina name=correo. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué recibirá PHP.

b) (0,40) Indica la corrección mínima.

c) (0,30) Explica qué mensaje de validación aparecería.

## UT2-043 — Correo inválido

Se introduce una cadena sin formato de correo. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace FILTER_VALIDATE_EMAIL.

b) (0,40) Indica qué bloque impide calcular el presupuesto.

c) (0,30) Explica qué debería conservar el formulario tras el error.

## UT2-044 — Límite de meses

El presupuesto admite de 1 a 24 meses. Variante: el nuevo límite solicitado es 27 meses.

a) (0,30) Explica qué ocurre con 25 meses.

b) (0,40) Indica los cambios necesarios para admitir hasta 36.

c) (0,30) Explica qué casos probarías.

## UT2-045 — Plan nuevo

Se quiere añadir un plan Premium de 12 euros al mes. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica dónde se valida el plan actualmente.

b) (0,40) Indica todos los bloques que habría que actualizar.

c) (0,30) Explica cómo probarías el cálculo y la selección.

## UT2-046 — Precio de extras

Backup cuesta 2 euros/mes y soporte 3 euros/mes. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Calcula el extra mensual con ambos marcados.

b) (0,40) Indica qué cambiarías si backup costara 4 euros.

c) (0,30) Explica una prueba con 6 meses.

## UT2-047 — Checkbox ausente

Un usuario no marca soporte. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué puede faltar $_POST[soporte].

b) (0,40) Indica cómo lo trata isset.

c) (0,30) Explica cómo probarías ambos estados.

## UT2-048 — Escapar HTML

El nombre del presupuesto se muestra con htmlspecialchars. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué riesgo reduce.

b) (0,40) Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML.

c) (0,30) Explica dónde más debe escaparse la salida.

## UT2-049 — Función de precios

obtenerPrecioPlan devuelve 5, 9 o 15. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la función.

b) (0,40) Indica cómo cambiarías el precio de Profesional a 11.

c) (0,30) Explica una prueba que detecte el cambio.

## UT2-050 — Login correcto

autenticar.php verifica usuario y contraseña con password_verify. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el flujo hasta panel.php.

b) (0,40) Indica qué datos se guardan en la sesión.

c) (0,30) Explica cómo comprobarías la redirección.

## UT2-051 — Login incorrecto

Un usuario introduce una contraseña incorrecta. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué ocurre con error_login.

b) (0,40) Indica qué página recibe la redirección.

c) (0,30) Explica cómo evitar mostrar información sensible.

## UT2-052 — Protección del panel

Un visitante abre panel.php sin sesión autenticada. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace la comprobación inicial.

b) (0,40) Indica qué cambiarías para proteger otra página privada.

c) (0,30) Explica cómo comprobarías que no se puede entrar.

## UT2-053 — Límite de notas

panel.php permite hasta 3 notas. Variante: el máximo solicitado es 6 notas.

a) (0,30) Explica dónde se controla el máximo.

b) (0,40) Indica el cambio mínimo para permitir 5.

c) (0,30) Explica qué probarías con 4, 5 y 6 notas.

## UT2-054 — Contador de accesos

panel.php incrementa accesos en GET salvo tras guardar una nota. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no cuenta el GET tras guardar.

b) (0,40) Indica qué variable de sesión interviene.

c) (0,30) Explica una secuencia de peticiones y su resultado.

## UT2-055 — Cerrar sesión

logout.php destruye la sesión y redirige. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué información deja de estar disponible.

b) (0,40) Indica qué ocurre al volver a panel.php.

c) (0,30) Explica cómo probarías el cierre.

## UT2-056 — Redirección PRG

Tras guardar una nota se redirige a panel.php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve POST-Redirect-GET.

b) (0,40) Razona qué pasaría al recargar si no se redirigiera.

c) (0,30) Indica cómo comprobarías que no se duplica la nota.

## UT2-057 — Sesiones aisladas

Ana y Marcos inician sesión desde navegadores diferentes. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica si comparten notas y contador.

b) (0,40) Indica qué estructura almacena los datos de cada sesión.

c) (0,30) Explica cómo verificarías el aislamiento.

## UT2-058 — Validación del nombre

El presupuesto recibe un nombre compuesto solo por espacios. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace trim.

b) (0,40) Indica qué validación lo rechaza.

c) (0,30) Explica cómo probarías la respuesta.

## UT2-059 — Número entero

El usuario introduce 2.5 meses. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué no es válido.

b) (0,40) Identifica la función usada para validarlo.

c) (0,30) Explica qué debería mostrarse en vez de un total.

## UT2-060 — Sesión tras login

El login llama a session_regenerate_id(true). Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve.

b) (0,40) Indica en qué momento se llama.

c) (0,30) Explica qué debe conservarse en la sesión después.
