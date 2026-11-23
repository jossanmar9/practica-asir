# Guía de Git y publicación de Práctica ASIR

El repositorio ya existe: https://github.com/jossanmar9/practica-asir

No es necesario crear otro repositorio ni ejecutar `git init`.

## Clonar y trabajar

```bash
git clone git@github.com:jossanmar9/practica-asir.git
cd practica-asir
git pull --ff-only
git switch -c mejora/ejercicios
# Edita los archivos
python3 scripts/generar_catalogo.py
git status
git add .
git diff --staged
git commit -m "Mejorar ejercicios y actualizar catálogo"
git push -u origin mejora/ejercicios
```

Abre una Pull Request para revisar los cambios antes de integrarlos en `main`.

## Publicar con GitHub Pages

1. Entra en **Settings → Pages** del repositorio.
2. Selecciona **Deploy from a branch**.
3. Elige **main**, carpeta **/(root)**, y guarda.
4. Cuando termine el despliegue, comprueba https://jossanmar9.github.io/practica-asir/.

La web es estática: utiliza `index.html`, `assets/` y `catalogo.json`. No requiere backend ni base de datos.

## Pruebas locales

```bash
python3 scripts/generar_catalogo.py
python3 -m http.server 8000
```

Abre http://localhost:8000. Revisa búsqueda, filtros, enunciados, tests, descarga y progreso local. Para validar la interfaz en móvil, utiliza las herramientas de desarrollo del navegador.

**No publiques contraseñas, datos personales ni soluciones privadas.** Comprueba `git status` y `git diff --staged` antes de confirmar cambios.
