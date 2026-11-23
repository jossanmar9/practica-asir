# UT1 — 60 casos de interpretación y modificación

Cada caso vale 1 punto: a) 0,30; b) 0,40; c) 0,30. Responde por escrito y justifica cómo comprobarías el cambio.

## UT1-001 — Recorrido de una petición

Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1-002 — Archivo estático

Un usuario solicita /manual.pdf desde la carpeta app. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1-003 — Puerto publicado

En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8081.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT1-004 — Variable ausente

El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-005 — Nombre de host

En index.php se cambia DB_HOST de db a localhost. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1-006 — Persistencia de MariaDB

El servicio db monta db_data:/var/lib/mysql. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT1-007 — Inicialización SQL

Se modifica sql/init.sql pero la tabla existente no cambia. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1-008 — PHP-FPM inaccesible

Nginx devuelve 502 al solicitar index.php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1-009 — Archivo Nginx

El archivo nginx/default.conf reenvía .php al servicio php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT1-010 — Montaje compartido

Nginx y PHP montan ./app:/var/www/html. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1-011 — Dockerfile PHP

El servicio PHP se construye desde ./php. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-012 — Consulta de prueba

index.php hace SELECT COUNT(*) FROM prueba. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT1-013 — Captura de errores

index.php usa try/catch(Throwable $e) y muestra KO. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1-014 — Dependencias

Nginx depende de php y php depende de db. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1-015 — Archivo .env.example

El repositorio incluye .env.example con nombres de variables. Variante 1: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.

## UT1-016 — Recorrido de una petición

Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1-017 — Archivo estático

Un usuario solicita /manual.pdf desde la carpeta app. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1-018 — Puerto publicado

En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8082.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT1-019 — Variable ausente

El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-020 — Nombre de host

En index.php se cambia DB_HOST de db a localhost. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1-021 — Persistencia de MariaDB

El servicio db monta db_data:/var/lib/mysql. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT1-022 — Inicialización SQL

Se modifica sql/init.sql pero la tabla existente no cambia. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1-023 — PHP-FPM inaccesible

Nginx devuelve 502 al solicitar index.php. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1-024 — Archivo Nginx

El archivo nginx/default.conf reenvía .php al servicio php. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT1-025 — Montaje compartido

Nginx y PHP montan ./app:/var/www/html. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1-026 — Dockerfile PHP

El servicio PHP se construye desde ./php. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-027 — Consulta de prueba

index.php hace SELECT COUNT(*) FROM prueba. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT1-028 — Captura de errores

index.php usa try/catch(Throwable $e) y muestra KO. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1-029 — Dependencias

Nginx depende de php y php depende de db. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1-030 — Archivo .env.example

El repositorio incluye .env.example con nombres de variables. Variante 2: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.

## UT1-031 — Recorrido de una petición

Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1-032 — Archivo estático

Un usuario solicita /manual.pdf desde la carpeta app. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1-033 — Puerto publicado

En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8083.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT1-034 — Variable ausente

El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-035 — Nombre de host

En index.php se cambia DB_HOST de db a localhost. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1-036 — Persistencia de MariaDB

El servicio db monta db_data:/var/lib/mysql. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT1-037 — Inicialización SQL

Se modifica sql/init.sql pero la tabla existente no cambia. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1-038 — PHP-FPM inaccesible

Nginx devuelve 502 al solicitar index.php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1-039 — Archivo Nginx

El archivo nginx/default.conf reenvía .php al servicio php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT1-040 — Montaje compartido

Nginx y PHP montan ./app:/var/www/html. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1-041 — Dockerfile PHP

El servicio PHP se construye desde ./php. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-042 — Consulta de prueba

index.php hace SELECT COUNT(*) FROM prueba. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT1-043 — Captura de errores

index.php usa try/catch(Throwable $e) y muestra KO. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1-044 — Dependencias

Nginx depende de php y php depende de db. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1-045 — Archivo .env.example

El repositorio incluye .env.example con nombres de variables. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.

## UT1-046 — Recorrido de una petición

Un usuario solicita /index.php y la aplicación consulta la tabla prueba. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el recorrido desde el navegador hasta la respuesta.

b) (0,40) Identifica qué componente modificarías si se sirviera el PHP como texto.

c) (0,30) Indica cómo verificarías el arreglo.

## UT1-047 — Archivo estático

Un usuario solicita /manual.pdf desde la carpeta app. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué servicios participan.

b) (0,40) Razona qué ocurre si MariaDB está detenido.

c) (0,30) Indica qué comprobarías ante un 404.

## UT1-048 — Puerto publicado

En compose.yaml figura ports: ["8080:80"] y el usuario intenta localhost:80. Variante: el puerto solicitado por el responsable es 8084.

a) (0,30) Explica qué significa el mapeo.

b) (0,40) Propón un cambio para acceder desde localhost:8081.

c) (0,30) Explica qué comprobación harías.

## UT1-049 — Variable ausente

El .env define DB_PASSWORD pero el servicio php no la declara en environment. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué getenv puede no recibirla.

b) (0,40) Propón el cambio mínimo sin escribir la contraseña real.

c) (0,30) Indica cómo comprobar que el servicio utiliza la configuración nueva.

## UT1-050 — Nombre de host

En index.php se cambia DB_HOST de db a localhost. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué significa localhost dentro del contenedor PHP.

b) (0,40) Corrige el valor adecuado según compose.yaml.

c) (0,30) Indica qué síntoma y evidencia esperarías.

## UT1-051 — Persistencia de MariaDB

El servicio db monta db_data:/var/lib/mysql. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica para qué sirve el volumen.

b) (0,40) Razona qué pasaría al recrear contenedores conservando el volumen.

c) (0,30) Explica cómo comprobarías la persistencia.

## UT1-052 — Inicialización SQL

Se modifica sql/init.sql pero la tabla existente no cambia. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica cuándo se ejecutan los scripts de inicialización de MariaDB.

b) (0,40) Propón una forma segura de aplicar el cambio a datos existentes.

c) (0,30) Indica cómo verificar el resultado sin borrar datos.

## UT1-053 — PHP-FPM inaccesible

Nginx devuelve 502 al solicitar index.php. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Identifica una causa compatible con el síntoma.

b) (0,40) Indica qué configuración o servicio revisarías primero.

c) (0,30) Explica qué logs o comprobación consultarías.

## UT1-054 — Archivo Nginx

El archivo nginx/default.conf reenvía .php al servicio php. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica el papel de fastcgi_pass.

b) (0,40) Razona qué cambiarías si el servicio se llamara backend.

c) (0,30) Indica cómo detectarías una referencia antigua.

## UT1-055 — Montaje compartido

Nginx y PHP montan ./app:/var/www/html. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué ambos necesitan acceder al código.

b) (0,40) Describe qué fallo podría producirse si PHP montara otra ruta.

c) (0,30) Explica cómo comprobarías el contenido disponible.

## UT1-056 — Dockerfile PHP

El servicio PHP se construye desde ./php. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica la diferencia entre build e image en este proyecto.

b) (0,40) Indica qué componente revisarías si faltara el controlador PDO MySQL.

c) (0,30) Explica cómo comprobarías que se ha reconstruido la imagen.

## UT1-057 — Consulta de prueba

index.php hace SELECT COUNT(*) FROM prueba. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué devuelve la consulta.

b) (0,40) Indica qué cambiarías si la tabla se llamara avisos.

c) (0,30) Explica qué verificarías en la base de datos.

## UT1-058 — Captura de errores

index.php usa try/catch(Throwable $e) y muestra KO. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1-059 — Dependencias

Nginx depende de php y php depende de db. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1-060 — Archivo .env.example

El repositorio incluye .env.example con nombres de variables. Variante 4: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.
