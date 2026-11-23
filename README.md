# Práctica ASIR · Preparación de exámenes

Material educativo para preparar ASO, Introducción a Python e Implantación de Aplicaciones Web (IAW) de ASIR. Los ejercicios de programación están **sin resolver** y los casos de IAW incluyen orientaciones de corrección por separado. No son materiales oficiales.

## Web de estudio

**[Abrir Práctica ASIR](https://jossanmar9.github.io/practica-asir/)**

La web permite buscar ejercicios, filtrar por asignatura y nivel, consultar enunciados, descargar archivos y marcar actividades como completadas. El progreso se guarda **solo en el navegador** mediante `localStorage`, no se sincroniza entre dispositivos. Puedes exportarlo a CSV desde el catálogo.

Para publicar los cambios, activa GitHub Pages en **Settings → Pages → Deploy from a branch → main / (root)**. La URL solo estará disponible cuando termine el despliegue.

## Contenido del repositorio

| Asignatura | Ejercicios y casos | Simulacros | Preguntas de test |
|---|---:|---:|---:|
| [ASO · Bash y procesos](ASO/) | 63 ejercicios temáticos | 10 × 2 scripts (20) | [200](ASO/banco_200_preguntas.json) |
| [Introducción a Python](Python/) | 100 para practicar + 75 para entregar | 10 × 5 scripts (50) | [480](Python/test_teorico/preguntas.json) |
| [IAW · PHP, Docker y MariaDB](IAW/) | 60 casos UT1 + 60 casos UT2 | 10 simulacros escritos | [240](IAW/05_Test_HTML/banco_240_preguntas.json) |

En total: **83 scripts Bash**, **225 scripts Python**, **120 casos IAW** y **10 simulacros escritos de IAW**. Los tres bancos suman **920 preguntas**. Las 480 preguntas de Python tienen enunciados distintos; el banco de IAW incluye reformulaciones de un número menor de conceptos.

### Tests autocorregibles

- [Test de ASO](ASO/test_aso_ut1_ut2.html)
- [Test de Python](Python/test_teorico/test_python_480_preguntas.html)
- [Test de IAW](IAW/05_Test_HTML/test_IAW.html)

Cada test HTML incluye internamente su banco para funcionar sin conexión. Los archivos JSON se entregan también por separado; **editar un JSON no actualiza automáticamente su HTML**. La penalización de −0,5 por fallo es una configuración de estudio, no una norma confirmada de todos los exámenes.

## Estructura

```text
practica-asir/
├── index.html                 # Portada de GitHub Pages
├── assets/                    # CSS y JavaScript
├── catalogo.json              # Índice de 438 recursos
├── scripts/generar_catalogo.py
├── ASO/                       # Bash, procesos y test
├── Python/                    # Ejercicios, simulacros y test
├── IAW/                       # Casos, simulacros y test
├── seguiment.csv              # Seguimiento manual (nombre histórico)
└── GUIA_GIT.md                # Guía de Git y publicación
```

## Cómo practicar

1. Elige una asignatura y un tema.
2. Abre el enunciado `.sh` o `.py` y escribe tu solución debajo de los comentarios.
3. Comprueba casos normales, límite e incorrectos. No uses datos personales reales ni privilegios innecesarios.
4. Marca el ejercicio como completado en la web o utiliza [`seguiment.csv`](seguiment.csv).
5. En IAW, responde por escrito qué ocurre, qué cambiarías y cómo verificarías el resultado.

Ejemplos:

```bash
bash ASO/01_basicos/01_variables/01_identificar_servidor.sh
python3 Python/ejercicios/UT1_variables_operaciones/practicar/01_conversión_de_unidades.py
```

## Actualizar el catálogo

Al añadir, mover o eliminar ejercicios, regenera el índice:

```bash
python3 scripts/generar_catalogo.py
git add catalogo.json
git commit -m "Actualizar catálogo de actividades"
git push
```

Para probar la portada localmente utiliza un servidor estático, porque abrir `index.html` mediante `file://` puede bloquear la lectura de `catalogo.json`:

```bash
python3 -m http.server 8000
# Abre http://localhost:8000
```

Los tests HTML sí pueden abrirse directamente en el navegador.

## Licencia y avisos

**Licencia pendiente de elección.** Hasta que se añada un archivo `LICENSE`, no se concede una licencia de reutilización del contenido por el mero hecho de que el repositorio sea público. No se ha asignado una licencia sin autorización del titular.

Revisa las guías de [ASO](ASO/README.md), [Python](Python/README.md) e [IAW](IAW/README.md). Los materiales pueden contener errores; las soluciones orientativas de IAW no son respuestas oficiales de la profesora.
