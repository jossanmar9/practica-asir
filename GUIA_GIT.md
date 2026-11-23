# Guia de Git i publicació de Pràctica ASIR

Aquest repositori **ja existeix**: https://github.com/jossanmar9/practica-asir

No cal crear un repositori buit ni tornar a executar `git init`.

## Clonar i treballar

```bash
git clone git@github.com:jossanmar9/practica-asir.git
cd practica-asir
git pull --ff-only
```

Fes els canvis en una branca de treball, especialment si modifiques exercicis o els tests:

```bash
git switch -c millora/exercicis
# modifica els fitxers
python3 scripts/generar_catalogo.py    # si has afegit/mogut/eliminat activitats
git add .
git commit -m "Millorar enunciats i actualitzar catàleg"
git push -u origin millora/exercicis
```

Pots obrir una pull request abans de fusionar a `main`.

## Com publicar la web en GitHub Pages

1. Obri **Settings → Pages** del repositori.
2. Selecciona **Deploy from a branch**.
3. Tria la branca **main**, carpeta **/(root)**, i guarda.
4. Quan GitHub indique el desplegament correcte, la web hauria d'estar disponible a **https://jossanmar9.github.io/practica-asir/**.

La web utilitza `index.html`, `assets/` i `catalogo.json`, sense backend ni base de dades.

## Proves en local

```bash
python3 scripts/generar_catalogo.py
python3 -m http.server 8000
```

Obri http://localhost:8000. Comprova cercador, filtres, previsualització d'enunciats, tests i progrés local.

**No faces `git add .` si dins de la carpeta has guardat secrets, dades personals o solucions privades.** Revisa sempre `git status` i `git diff --staged` abans de confirmar canvis.
