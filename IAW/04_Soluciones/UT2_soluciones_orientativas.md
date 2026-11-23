# Soluciones orientativas — UT2

## UT2-001 — GET y POST

Orientación de corrección: a) describir con precisión el flujo o el efecto en «GET y POST»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué sucede en la primera visita GET. Indica qué cambiarías si el formulario enviara GET por error. Explica cómo verificarías el envío.

## UT2-002 — Atributo name

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Atributo name»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué recibirá PHP. Indica la corrección mínima. Explica qué mensaje de validación aparecería.

## UT2-003 — Correo inválido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Correo inválido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace FILTER_VALIDATE_EMAIL. Indica qué bloque impide calcular el presupuesto. Explica qué debería conservar el formulario tras el error.

## UT2-004 — Límite de meses

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de meses»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con 25 meses. Indica los cambios necesarios para admitir hasta 36. Explica qué casos probarías.

## UT2-005 — Plan nuevo

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Plan nuevo»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se valida el plan actualmente. Indica todos los bloques que habría que actualizar. Explica cómo probarías el cálculo y la selección.

## UT2-006 — Precio de extras

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Precio de extras»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Calcula el extra mensual con ambos marcados. Indica qué cambiarías si backup costara 4 euros. Explica una prueba con 6 meses.

## UT2-007 — Checkbox ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Checkbox ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué puede faltar $_POST[soporte]. Indica cómo lo trata isset. Explica cómo probarías ambos estados.

## UT2-008 — Escapar HTML

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Escapar HTML»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué riesgo reduce. Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML. Explica dónde más debe escaparse la salida.

## UT2-009 — Función de precios

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Función de precios»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la función. Indica cómo cambiarías el precio de Profesional a 11. Explica una prueba que detecte el cambio.

## UT2-010 — Login correcto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login correcto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el flujo hasta panel.php. Indica qué datos se guardan en la sesión. Explica cómo comprobarías la redirección.

## UT2-011 — Login incorrecto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login incorrecto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con error_login. Indica qué página recibe la redirección. Explica cómo evitar mostrar información sensible.

## UT2-012 — Protección del panel

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Protección del panel»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la comprobación inicial. Indica qué cambiarías para proteger otra página privada. Explica cómo comprobarías que no se puede entrar.

## UT2-013 — Límite de notas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de notas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se controla el máximo. Indica el cambio mínimo para permitir 5. Explica qué probarías con 4, 5 y 6 notas.

## UT2-014 — Contador de accesos

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Contador de accesos»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no cuenta el GET tras guardar. Indica qué variable de sesión interviene. Explica una secuencia de peticiones y su resultado.

## UT2-015 — Cerrar sesión

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Cerrar sesión»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué información deja de estar disponible. Indica qué ocurre al volver a panel.php. Explica cómo probarías el cierre.

## UT2-016 — Redirección PRG

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Redirección PRG»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve POST-Redirect-GET. Razona qué pasaría al recargar si no se redirigiera. Indica cómo comprobarías que no se duplica la nota.

## UT2-017 — Sesiones aisladas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesiones aisladas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica si comparten notas y contador. Indica qué estructura almacena los datos de cada sesión. Explica cómo verificarías el aislamiento.

## UT2-018 — Validación del nombre

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Validación del nombre»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace trim. Indica qué validación lo rechaza. Explica cómo probarías la respuesta.

## UT2-019 — Número entero

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Número entero»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no es válido. Identifica la función usada para validarlo. Explica qué debería mostrarse en vez de un total.

## UT2-020 — Sesión tras login

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesión tras login»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve. Indica en qué momento se llama. Explica qué debe conservarse en la sesión después.

## UT2-021 — GET y POST

Orientación de corrección: a) describir con precisión el flujo o el efecto en «GET y POST»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué sucede en la primera visita GET. Indica qué cambiarías si el formulario enviara GET por error. Explica cómo verificarías el envío.

## UT2-022 — Atributo name

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Atributo name»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué recibirá PHP. Indica la corrección mínima. Explica qué mensaje de validación aparecería.

## UT2-023 — Correo inválido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Correo inválido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace FILTER_VALIDATE_EMAIL. Indica qué bloque impide calcular el presupuesto. Explica qué debería conservar el formulario tras el error.

## UT2-024 — Límite de meses

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de meses»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con 25 meses. Indica los cambios necesarios para admitir hasta 36. Explica qué casos probarías.

## UT2-025 — Plan nuevo

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Plan nuevo»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se valida el plan actualmente. Indica todos los bloques que habría que actualizar. Explica cómo probarías el cálculo y la selección.

## UT2-026 — Precio de extras

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Precio de extras»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Calcula el extra mensual con ambos marcados. Indica qué cambiarías si backup costara 4 euros. Explica una prueba con 6 meses.

## UT2-027 — Checkbox ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Checkbox ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué puede faltar $_POST[soporte]. Indica cómo lo trata isset. Explica cómo probarías ambos estados.

## UT2-028 — Escapar HTML

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Escapar HTML»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué riesgo reduce. Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML. Explica dónde más debe escaparse la salida.

## UT2-029 — Función de precios

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Función de precios»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la función. Indica cómo cambiarías el precio de Profesional a 11. Explica una prueba que detecte el cambio.

## UT2-030 — Login correcto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login correcto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el flujo hasta panel.php. Indica qué datos se guardan en la sesión. Explica cómo comprobarías la redirección.

## UT2-031 — Login incorrecto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login incorrecto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con error_login. Indica qué página recibe la redirección. Explica cómo evitar mostrar información sensible.

## UT2-032 — Protección del panel

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Protección del panel»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la comprobación inicial. Indica qué cambiarías para proteger otra página privada. Explica cómo comprobarías que no se puede entrar.

## UT2-033 — Límite de notas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de notas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se controla el máximo. Indica el cambio mínimo para permitir 5. Explica qué probarías con 4, 5 y 6 notas.

## UT2-034 — Contador de accesos

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Contador de accesos»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no cuenta el GET tras guardar. Indica qué variable de sesión interviene. Explica una secuencia de peticiones y su resultado.

## UT2-035 — Cerrar sesión

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Cerrar sesión»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué información deja de estar disponible. Indica qué ocurre al volver a panel.php. Explica cómo probarías el cierre.

## UT2-036 — Redirección PRG

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Redirección PRG»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve POST-Redirect-GET. Razona qué pasaría al recargar si no se redirigiera. Indica cómo comprobarías que no se duplica la nota.

## UT2-037 — Sesiones aisladas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesiones aisladas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica si comparten notas y contador. Indica qué estructura almacena los datos de cada sesión. Explica cómo verificarías el aislamiento.

## UT2-038 — Validación del nombre

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Validación del nombre»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace trim. Indica qué validación lo rechaza. Explica cómo probarías la respuesta.

## UT2-039 — Número entero

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Número entero»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no es válido. Identifica la función usada para validarlo. Explica qué debería mostrarse en vez de un total.

## UT2-040 — Sesión tras login

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesión tras login»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve. Indica en qué momento se llama. Explica qué debe conservarse en la sesión después.

## UT2-041 — GET y POST

Orientación de corrección: a) describir con precisión el flujo o el efecto en «GET y POST»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué sucede en la primera visita GET. Indica qué cambiarías si el formulario enviara GET por error. Explica cómo verificarías el envío.

## UT2-042 — Atributo name

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Atributo name»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué recibirá PHP. Indica la corrección mínima. Explica qué mensaje de validación aparecería.

## UT2-043 — Correo inválido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Correo inválido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace FILTER_VALIDATE_EMAIL. Indica qué bloque impide calcular el presupuesto. Explica qué debería conservar el formulario tras el error.

## UT2-044 — Límite de meses

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de meses»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con 25 meses. Indica los cambios necesarios para admitir hasta 36. Explica qué casos probarías.

## UT2-045 — Plan nuevo

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Plan nuevo»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se valida el plan actualmente. Indica todos los bloques que habría que actualizar. Explica cómo probarías el cálculo y la selección.

## UT2-046 — Precio de extras

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Precio de extras»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Calcula el extra mensual con ambos marcados. Indica qué cambiarías si backup costara 4 euros. Explica una prueba con 6 meses.

## UT2-047 — Checkbox ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Checkbox ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué puede faltar $_POST[soporte]. Indica cómo lo trata isset. Explica cómo probarías ambos estados.

## UT2-048 — Escapar HTML

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Escapar HTML»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué riesgo reduce. Indica qué ocurriría si se mostrara directamente un texto con etiquetas HTML. Explica dónde más debe escaparse la salida.

## UT2-049 — Función de precios

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Función de precios»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la función. Indica cómo cambiarías el precio de Profesional a 11. Explica una prueba que detecte el cambio.

## UT2-050 — Login correcto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login correcto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el flujo hasta panel.php. Indica qué datos se guardan en la sesión. Explica cómo comprobarías la redirección.

## UT2-051 — Login incorrecto

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Login incorrecto»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué ocurre con error_login. Indica qué página recibe la redirección. Explica cómo evitar mostrar información sensible.

## UT2-052 — Protección del panel

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Protección del panel»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace la comprobación inicial. Indica qué cambiarías para proteger otra página privada. Explica cómo comprobarías que no se puede entrar.

## UT2-053 — Límite de notas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Límite de notas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica dónde se controla el máximo. Indica el cambio mínimo para permitir 5. Explica qué probarías con 4, 5 y 6 notas.

## UT2-054 — Contador de accesos

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Contador de accesos»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no cuenta el GET tras guardar. Indica qué variable de sesión interviene. Explica una secuencia de peticiones y su resultado.

## UT2-055 — Cerrar sesión

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Cerrar sesión»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué información deja de estar disponible. Indica qué ocurre al volver a panel.php. Explica cómo probarías el cierre.

## UT2-056 — Redirección PRG

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Redirección PRG»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve POST-Redirect-GET. Razona qué pasaría al recargar si no se redirigiera. Indica cómo comprobarías que no se duplica la nota.

## UT2-057 — Sesiones aisladas

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesiones aisladas»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica si comparten notas y contador. Indica qué estructura almacena los datos de cada sesión. Explica cómo verificarías el aislamiento.

## UT2-058 — Validación del nombre

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Validación del nombre»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué hace trim. Indica qué validación lo rechaza. Explica cómo probarías la respuesta.

## UT2-059 — Número entero

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Número entero»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué no es válido. Identifica la función usada para validarlo. Explica qué debería mostrarse en vez de un total.

## UT2-060 — Sesión tras login

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Sesión tras login»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve. Indica en qué momento se llama. Explica qué debe conservarse en la sesión después.
