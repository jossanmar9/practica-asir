# Publicar el repositori a GitHub

1. Crea el repositori buit `practica-asir` a GitHub (preferiblement **sense** README, `.gitignore` ni llicència inicials).
2. Descomprimeix el ZIP i obri un terminal **dins de la carpeta `practica-asir`**.
3. Executa:

```bash
git init
git branch -M main
git add .
git commit -m "Afegir 300 exercicis de Bash i Python"
git remote add origin git@github.com:jossanmar9/practica-asir.git
git push -u origin main
```

Si has creat el repositori amb un README inicial, serà més senzill clonar-lo i copiar-hi el contingut d'esta carpeta abans de fer `git add .`.

Per a enviar avanços més endavant:

```bash
git add .
git commit -m "Resoldre exercicis del primer bloc"
git push
```

No publiques contrasenyes, claus ni informació personal dins de les solucions.
