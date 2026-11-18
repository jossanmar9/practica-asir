# Pràctica ASIR · Entrenament d'exàmens

Repositori d'exercicis pràctics per a **2n d'ASIR**, pensat per a aprendre programant, equivocar-se, corregir i repetir.

## Contingut

| Àrea | Carpetes | Exercicis |
|---|---:|---:|
| [ASO · Bash](ASO/Bash/) | 8 blocs | 120 scripts `.sh` |
| [Python](Python/) | 9 blocs | 180 scripts `.py` |
| [IAW](IAW/) | 10 blocs | 100 casos `.md` |

**Total: 400 activitats sense resoldre (300 scripts + 100 casos de raonament).** Els enunciats de Bash i Python estan dins de cada fitxer com a comentaris; els d’IAW són documents Markdown. Les dades de prova de Bash estan a `ASO/Bash/dades_prova/`.

Per a IAW, l’examen és escrit i no requerix executar codi: respon els apartats a), b) i c) de cada cas i justifica com comprovaries la solució. Consulta [la guia d’IAW](IAW/README.md).

## Mètode de treball

1. Obri una carpeta de bloc amb VS Code.
2. Llig l'enunciat del fitxer `.sh` o `.py` i escriu la solució a continuació dels comentaris.
3. Executa'l amb casos normals, incorrectes i límit.
4. Marca l'estat a [`seguiment.csv`](seguiment.csv) (`pendent`, `en_progres`, `revisar`, `superat`).
5. Envia els scripts resolts per a corregir-los i torna a provar els que fallen.

## Execució

```bash
# Bash
bash ASO/Bash/01_fonaments/02_copiar_logs.sh origen desti

# Python
python3 Python/04_condicionals/02_port_reservat.py
```

Adapta els arguments a l'enunciat. **No executes com a administrador** scripts que encara no has revisat. Utilitza carpetes de prova i no dades reals.

## Procedència i abast

- Bash: exercicis nous inspirats en les pràctiques d'Administració de Sistemes Operatius (ASO).
- Python: exercicis nous basats en els conceptes de les UT1, UT2 i UT3 de [Python Intro Alumnos](https://victoria-nr.github.io/python-intro-alumnos/).
- IAW: casos originals de raonament segons el format indicat per la professora per a UT1 i UT2.
- No hi ha generadors ni automatitzacions que sobreescriguen les teues solucions.

Els exercicis són material de pràctica addicional, no còpies literals dels enunciats de classe.
