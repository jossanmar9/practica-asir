# Pràctica ASIR · Entrenament d'exàmens

Material educatiu de **2n d'ASIR** per a preparar els exàmens d'ASO, Introducció a Python i Implantació d'Aplicacions Web (IAW). Els exercicis de programació estan **sense resoldre**; els casos d'IAW inclouen orientacions de correcció separades. No són materials oficials.

## 🌐 Web d'estudi

La portada de la web és [`index.html`](index.html). Funciona com a catàleg de totes les activitats i enllaça als tests de cada assignatura.

Quan s'active GitHub Pages per a la branca `main`, l'adreça prevista serà:

**https://jossanmar9.github.io/practica-asir/**

Per activar-lo: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**. La URL no es considera publicada fins que GitHub Pages confirme el desplegament.

La web permet cercar exercicis, filtrar per assignatura i nivell, llegir els enunciats i marcar-los com a superats. **El progrés es guarda al navegador amb `localStorage`**, no s'envia a GitHub ni se sincronitza entre dispositius.

## 📚 Contingut real del repositori

| Assignatura | Exercicis i casos | Simulacres | Banc de test |
|---|---:|---:|---:|
| [ASO · Bash i processos](ASO/) | 63 exercicis temàtics | 10 × 2 scripts (20) | [200 preguntes](ASO/banco_200_preguntas.json) |
| [Introducció a Python](Python/) | 100 «practicar» + 75 «entregar» | 10 × 5 scripts (50) | [480 preguntes](Python/test_teorico/preguntas.json) |
| [IAW · PHP, Docker i MariaDB](IAW/) | 60 casos UT1 + 60 casos UT2 | 10 simulacres de 6 casos | [240 preguntes](IAW/05_Test_HTML/banco_240_preguntas.json) |

**Fitxers d'activitats:** 83 scripts `.sh`, 225 scripts `.py`, 120 casos escrits d'IAW en dos documents i 10 simulacres escrits d'IAW. Hi ha **920 ítems de test**, que inclouen reformulacions de conceptes i no equivalen a 920 coneixements diferents.

### Tests interactius

- [Test ASO — UT1 i UT2](ASO/test_aso_ut1_ut2.html)
- [Test Python — cadenes, condicionals, while i for](Python/test_teorico/test_python_480_preguntas.html)
- [Test IAW — UT1 i UT2](IAW/05_Test_HTML/test_IAW.html)

Cada HTML incorpora el seu banc i funciona també si es descarrega i s'obri localment sense servidor. Els fitxers JSON són còpies dels bancs per a consulta i reutilització: **canviar un JSON no modifica automàticament el test HTML corresponent**. La penalització de −0,5 per resposta incorrecta s'utilitza per a practicar, i no confirma la puntuació real dels exàmens.

## 🗂️ Organització

```text
practica-asir/
├── index.html                 # Portada de la web (GitHub Pages)
├── assets/                    # Estils i lògica del cercador
├── catalogo.json              # Índex de fitxers i casos que mostra la web
├── scripts/generar_catalogo.py
├── ASO/                       # Bash, processos, 10 simulacres i test
├── Python/                    # UT1, UT2, UT3, simulacres i test
├── IAW/                       # Casos, simulacres, solucions i test
├── seguiment.csv              # Full de seguiment manual
└── GUIA_GIT.md                # Guia d'edició i publicació
```

## ▶️ Com practicar

1. Tria una assignatura i un tema des de la web o des de les carpetes.
2. Llig l'enunciat del fitxer `.sh` o `.py` i escriu la solució a continuació dels comentaris.
3. Prova casos normals, límit i incorrectes. No uses privilegis d'administrador ni dades de producció.
4. Marca l'exercici com a superat en la web o anota els intents a [`seguiment.csv`](seguiment.csv).
5. Per a IAW, respon els apartats a), b) i c) per escrit, justificant sempre la comprovació que faries.

Exemples d'execució:

```bash
bash ASO/01_basicos/01_variables/01_identificar_servidor.sh
python3 Python/ejercicios/UT1_variables_operaciones/practicar/01_conversión_de_unidades.py
```

## 🔧 Mantindre el catàleg

La web no accedix a l'API de GitHub en cada visita: llig el fitxer local `catalogo.json`. Quan s'afegisquen, es moguen o s'eliminen activitats, cal regenerar-lo:

```bash
python3 scripts/generar_catalogo.py
git add catalogo.json
git commit -m "Actualitzar catàleg d'activitats"
git push
```

Per al desenvolupament local de la **portada web**, utilitza un servidor estàtic (obrir `index.html` amb `file://` pot impedir que `fetch()` llija `catalogo.json`):

```bash
python3 -m http.server 8000
# Obri http://localhost:8000
```

Els tres tests HTML, en canvi, es poden obrir directament amb el navegador.

## 📖 Origen i avisos

Materials propis per a practicar a partir dels temes, exemples i pràctiques del mòdul. Consulta les guies [d'ASO](ASO/README.md), [de Python](Python/README.md) i [d'IAW](IAW/README.md) per al detall. La revisió dels enunciats i dels bancs de preguntes és un procés continu; poden existir preguntes repetitives o variants millorables. Les solucions orientatives d'IAW no són respostes oficials de la professora.

No inclogues contrasenyes, claus ni informació personal en els exercicis, commits o incidències.
