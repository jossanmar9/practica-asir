# Soluciones orientativas — UT1

## UT1-001 — Recorrido de una petición

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Recorrido de una petición»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el recorrido desde el navegador hasta la respuesta. Identifica qué componente modificarías si se sirviera el PHP como texto. Indica cómo verificarías el arreglo.

## UT1-002 — Archivo estático

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo estático»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué servicios participan. Razona qué ocurre si MariaDB está detenido. Indica qué comprobarías ante un 404.

## UT1-003 — Puerto publicado

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Puerto publicado»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa el mapeo. Propón un cambio para acceder desde localhost:8081. Explica qué comprobación harías.

## UT1-004 — Variable ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Variable ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué getenv puede no recibirla. Propón el cambio mínimo sin escribir la contraseña real. Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-005 — Nombre de host

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Nombre de host»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa localhost dentro del contenedor PHP. Corrige el valor adecuado según compose.yaml. Indica qué síntoma y evidencia esperarías.

## UT1-006 — Persistencia de MariaDB

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Persistencia de MariaDB»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve el volumen. Razona qué pasaría al recrear contenedores conservando el volumen. Explica cómo comprobarías la persistencia.

## UT1-007 — Inicialización SQL

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Inicialización SQL»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica cuándo se ejecutan los scripts de inicialización de MariaDB. Propón una forma segura de aplicar el cambio a datos existentes. Indica cómo verificar el resultado sin borrar datos.

## UT1-008 — PHP-FPM inaccesible

Orientación de corrección: a) describir con precisión el flujo o el efecto en «PHP-FPM inaccesible»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Identifica una causa compatible con el síntoma. Indica qué configuración o servicio revisarías primero. Explica qué logs o comprobación consultarías.

## UT1-009 — Archivo Nginx

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo Nginx»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el papel de fastcgi_pass. Razona qué cambiarías si el servicio se llamara backend. Indica cómo detectarías una referencia antigua.

## UT1-010 — Montaje compartido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Montaje compartido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué ambos necesitan acceder al código. Describe qué fallo podría producirse si PHP montara otra ruta. Explica cómo comprobarías el contenido disponible.

## UT1-011 — Dockerfile PHP

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dockerfile PHP»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica la diferencia entre build e image en este proyecto. Indica qué componente revisarías si faltara el controlador PDO MySQL. Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-012 — Consulta de prueba

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Consulta de prueba»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué devuelve la consulta. Indica qué cambiarías si la tabla se llamara avisos. Explica qué verificarías en la base de datos.

## UT1-013 — Captura de errores

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Captura de errores»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué la página puede cargar aunque falle la base de datos. Propón cómo diagnosticar el fallo sin mostrar secretos al visitante. Indica qué salida esperas ante conexión fallida.

## UT1-014 — Dependencias

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dependencias»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué organiza depends_on. Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas. Indica qué evidencia revisarías.

## UT1-015 — Archivo .env.example

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo .env.example»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica su finalidad. Indica qué no se debe incluir en ese archivo. Explica cómo prepararías un entorno nuevo.

## UT1-016 — Recorrido de una petición

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Recorrido de una petición»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el recorrido desde el navegador hasta la respuesta. Identifica qué componente modificarías si se sirviera el PHP como texto. Indica cómo verificarías el arreglo.

## UT1-017 — Archivo estático

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo estático»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué servicios participan. Razona qué ocurre si MariaDB está detenido. Indica qué comprobarías ante un 404.

## UT1-018 — Puerto publicado

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Puerto publicado»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa el mapeo. Propón un cambio para acceder desde localhost:8081. Explica qué comprobación harías.

## UT1-019 — Variable ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Variable ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué getenv puede no recibirla. Propón el cambio mínimo sin escribir la contraseña real. Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-020 — Nombre de host

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Nombre de host»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa localhost dentro del contenedor PHP. Corrige el valor adecuado según compose.yaml. Indica qué síntoma y evidencia esperarías.

## UT1-021 — Persistencia de MariaDB

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Persistencia de MariaDB»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve el volumen. Razona qué pasaría al recrear contenedores conservando el volumen. Explica cómo comprobarías la persistencia.

## UT1-022 — Inicialización SQL

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Inicialización SQL»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica cuándo se ejecutan los scripts de inicialización de MariaDB. Propón una forma segura de aplicar el cambio a datos existentes. Indica cómo verificar el resultado sin borrar datos.

## UT1-023 — PHP-FPM inaccesible

Orientación de corrección: a) describir con precisión el flujo o el efecto en «PHP-FPM inaccesible»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Identifica una causa compatible con el síntoma. Indica qué configuración o servicio revisarías primero. Explica qué logs o comprobación consultarías.

## UT1-024 — Archivo Nginx

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo Nginx»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el papel de fastcgi_pass. Razona qué cambiarías si el servicio se llamara backend. Indica cómo detectarías una referencia antigua.

## UT1-025 — Montaje compartido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Montaje compartido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué ambos necesitan acceder al código. Describe qué fallo podría producirse si PHP montara otra ruta. Explica cómo comprobarías el contenido disponible.

## UT1-026 — Dockerfile PHP

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dockerfile PHP»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica la diferencia entre build e image en este proyecto. Indica qué componente revisarías si faltara el controlador PDO MySQL. Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-027 — Consulta de prueba

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Consulta de prueba»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué devuelve la consulta. Indica qué cambiarías si la tabla se llamara avisos. Explica qué verificarías en la base de datos.

## UT1-028 — Captura de errores

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Captura de errores»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué la página puede cargar aunque falle la base de datos. Propón cómo diagnosticar el fallo sin mostrar secretos al visitante. Indica qué salida esperas ante conexión fallida.

## UT1-029 — Dependencias

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dependencias»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué organiza depends_on. Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas. Indica qué evidencia revisarías.

## UT1-030 — Archivo .env.example

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo .env.example»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica su finalidad. Indica qué no se debe incluir en ese archivo. Explica cómo prepararías un entorno nuevo.

## UT1-031 — Recorrido de una petición

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Recorrido de una petición»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el recorrido desde el navegador hasta la respuesta. Identifica qué componente modificarías si se sirviera el PHP como texto. Indica cómo verificarías el arreglo.

## UT1-032 — Archivo estático

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo estático»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué servicios participan. Razona qué ocurre si MariaDB está detenido. Indica qué comprobarías ante un 404.

## UT1-033 — Puerto publicado

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Puerto publicado»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa el mapeo. Propón un cambio para acceder desde localhost:8081. Explica qué comprobación harías.

## UT1-034 — Variable ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Variable ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué getenv puede no recibirla. Propón el cambio mínimo sin escribir la contraseña real. Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-035 — Nombre de host

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Nombre de host»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa localhost dentro del contenedor PHP. Corrige el valor adecuado según compose.yaml. Indica qué síntoma y evidencia esperarías.

## UT1-036 — Persistencia de MariaDB

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Persistencia de MariaDB»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve el volumen. Razona qué pasaría al recrear contenedores conservando el volumen. Explica cómo comprobarías la persistencia.

## UT1-037 — Inicialización SQL

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Inicialización SQL»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica cuándo se ejecutan los scripts de inicialización de MariaDB. Propón una forma segura de aplicar el cambio a datos existentes. Indica cómo verificar el resultado sin borrar datos.

## UT1-038 — PHP-FPM inaccesible

Orientación de corrección: a) describir con precisión el flujo o el efecto en «PHP-FPM inaccesible»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Identifica una causa compatible con el síntoma. Indica qué configuración o servicio revisarías primero. Explica qué logs o comprobación consultarías.

## UT1-039 — Archivo Nginx

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo Nginx»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el papel de fastcgi_pass. Razona qué cambiarías si el servicio se llamara backend. Indica cómo detectarías una referencia antigua.

## UT1-040 — Montaje compartido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Montaje compartido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué ambos necesitan acceder al código. Describe qué fallo podría producirse si PHP montara otra ruta. Explica cómo comprobarías el contenido disponible.

## UT1-041 — Dockerfile PHP

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dockerfile PHP»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica la diferencia entre build e image en este proyecto. Indica qué componente revisarías si faltara el controlador PDO MySQL. Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-042 — Consulta de prueba

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Consulta de prueba»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué devuelve la consulta. Indica qué cambiarías si la tabla se llamara avisos. Explica qué verificarías en la base de datos.

## UT1-043 — Captura de errores

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Captura de errores»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué la página puede cargar aunque falle la base de datos. Propón cómo diagnosticar el fallo sin mostrar secretos al visitante. Indica qué salida esperas ante conexión fallida.

## UT1-044 — Dependencias

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dependencias»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué organiza depends_on. Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas. Indica qué evidencia revisarías.

## UT1-045 — Archivo .env.example

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo .env.example»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica su finalidad. Indica qué no se debe incluir en ese archivo. Explica cómo prepararías un entorno nuevo.

## UT1-046 — Recorrido de una petición

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Recorrido de una petición»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el recorrido desde el navegador hasta la respuesta. Identifica qué componente modificarías si se sirviera el PHP como texto. Indica cómo verificarías el arreglo.

## UT1-047 — Archivo estático

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo estático»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué servicios participan. Razona qué ocurre si MariaDB está detenido. Indica qué comprobarías ante un 404.

## UT1-048 — Puerto publicado

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Puerto publicado»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa el mapeo. Propón un cambio para acceder desde localhost:8081. Explica qué comprobación harías.

## UT1-049 — Variable ausente

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Variable ausente»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué getenv puede no recibirla. Propón el cambio mínimo sin escribir la contraseña real. Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-050 — Nombre de host

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Nombre de host»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué significa localhost dentro del contenedor PHP. Corrige el valor adecuado según compose.yaml. Indica qué síntoma y evidencia esperarías.

## UT1-051 — Persistencia de MariaDB

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Persistencia de MariaDB»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica para qué sirve el volumen. Razona qué pasaría al recrear contenedores conservando el volumen. Explica cómo comprobarías la persistencia.

## UT1-052 — Inicialización SQL

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Inicialización SQL»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica cuándo se ejecutan los scripts de inicialización de MariaDB. Propón una forma segura de aplicar el cambio a datos existentes. Indica cómo verificar el resultado sin borrar datos.

## UT1-053 — PHP-FPM inaccesible

Orientación de corrección: a) describir con precisión el flujo o el efecto en «PHP-FPM inaccesible»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Identifica una causa compatible con el síntoma. Indica qué configuración o servicio revisarías primero. Explica qué logs o comprobación consultarías.

## UT1-054 — Archivo Nginx

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo Nginx»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica el papel de fastcgi_pass. Razona qué cambiarías si el servicio se llamara backend. Indica cómo detectarías una referencia antigua.

## UT1-055 — Montaje compartido

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Montaje compartido»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué ambos necesitan acceder al código. Describe qué fallo podría producirse si PHP montara otra ruta. Explica cómo comprobarías el contenido disponible.

## UT1-056 — Dockerfile PHP

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dockerfile PHP»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica la diferencia entre build e image en este proyecto. Indica qué componente revisarías si faltara el controlador PDO MySQL. Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-057 — Consulta de prueba

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Consulta de prueba»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué devuelve la consulta. Indica qué cambiarías si la tabla se llamara avisos. Explica qué verificarías en la base de datos.

## UT1-058 — Captura de errores

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Captura de errores»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica por qué la página puede cargar aunque falle la base de datos. Propón cómo diagnosticar el fallo sin mostrar secretos al visitante. Indica qué salida esperas ante conexión fallida.

## UT1-059 — Dependencias

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Dependencias»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica qué organiza depends_on. Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas. Indica qué evidencia revisarías.

## UT1-060 — Archivo .env.example

Orientación de corrección: a) describir con precisión el flujo o el efecto en «Archivo .env.example»; b) localizar el archivo y bloque afectados, proponer el cambio mínimo coherente con el proyecto; c) especificar entrada, resultado esperado y evidencia (navegador, configuración, logs o sesión según corresponda). No basta decir «lo revisaría»: debe citarse la comprobación concreta. Respuesta de referencia: Explica su finalidad. Indica qué no se debe incluir en ese archivo. Explica cómo prepararías un entorno nuevo.
