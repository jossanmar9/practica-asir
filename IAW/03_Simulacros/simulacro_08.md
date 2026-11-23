# Simulacro IAW 08

6 casos × 1 punto = 6 puntos. Tiempo sugerido: 60 minutos. Responde sin ejecutar código.

## UT1 — Captura de errores
index.php usa try/catch(Throwable $e) y muestra KO. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica por qué la página puede cargar aunque falle la base de datos.

b) (0,40) Propón cómo diagnosticar el fallo sin mostrar secretos al visitante.

c) (0,30) Indica qué salida esperas ante conexión fallida.

## UT1 — Dependencias
Nginx depende de php y php depende de db. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué organiza depends_on.

b) (0,40) Razona por qué no garantiza por sí solo que MariaDB esté lista para consultas.

c) (0,30) Indica qué evidencia revisarías.

## UT1 — Archivo .env.example
El repositorio incluye .env.example con nombres de variables. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica su finalidad.

b) (0,40) Indica qué no se debe incluir en ese archivo.

c) (0,30) Explica cómo prepararías un entorno nuevo.

## UT2 — Correo inválido
Se introduce una cadena sin formato de correo. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica qué hace FILTER_VALIDATE_EMAIL.

b) (0,40) Indica qué bloque impide calcular el presupuesto.

c) (0,30) Explica qué debería conservar el formulario tras el error.

## UT2 — Límite de meses
El presupuesto admite de 1 a 24 meses. Variante: el nuevo límite solicitado es 27 meses.

a) (0,30) Explica qué ocurre con 25 meses.

b) (0,40) Indica los cambios necesarios para admitir hasta 36.

c) (0,30) Explica qué casos probarías.

## UT2 — Plan nuevo
Se quiere añadir un plan Premium de 12 euros al mes. Variante 3: analiza también el caso de un cambio parcial que deje una referencia antigua o un dato no válido; no supongas que el resto del sistema falla.

a) (0,30) Explica dónde se valida el plan actualmente.

b) (0,40) Indica todos los bloques que habría que actualizar.

c) (0,30) Explica cómo probarías el cálculo y la selección.
