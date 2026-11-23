#!/usr/bin/env python3
"""Regenera catalogo.json a partir de los enunciados reales del repositorio.

Solo requiere Python 3 (biblioteca estándar). Ejecútalo desde
cualquier carpeta: python3 scripts/generar_catalogo.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def titol(nom: str) -> str:
    nom = re.sub(r"^\d+_", "", nom)
    nom = re.sub(r"\.[^.]+$", "", nom)
    return nom.replace("_", " ").strip().capitalize()


def afegir_fitxer(catalog: list[dict], path: Path, area: str, unit: str, level: str) -> None:
    relative = path.relative_to(ROOT).as_posix()
    catalog.append(
        {"path": relative, "title": titol(path.name), "area": area, "unit": unit, "level": level}
    )


def main() -> None:
    catalog: list[dict] = []

    for path in sorted((ROOT / "ASO").rglob("*.sh")):
        parts = path.relative_to(ROOT).parts
        section = parts[1]
        if section == "01_basicos":
            unit = titol(parts[2])
        elif section == "06_simulacros":
            unit = "Simulacros"
        else:
            unit = titol(section)
        level = "Simulacro" if section == "06_simulacros" else "Otros"
        afegir_fitxer(catalog, path, "ASO", unit, level)

    for path in sorted((ROOT / "Python").rglob("*.py")):
        parts = path.relative_to(ROOT).parts
        if parts[1] == "simulacros":
            unit, level = titol(parts[2]), "Simulacro"
        else:
            unit = titol(parts[2])
            level = {"practicar": "Practicar", "entregar": "Entregar"}.get(parts[-2], "Otros")
        afegir_fitxer(catalog, path, "Python", unit, level)

    for unit, relative in (
        ("UT1", "IAW/01_Casos_UT1/UT1_60_casos.md"),
        ("UT2", "IAW/02_Casos_UT2/UT2_60_casos.md"),
    ):
        path = ROOT / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        headings = re.findall(r"^##\s+(UT[12]-\d+)\s*[—–-]\s*(.*)$", content, flags=re.MULTILINE)
        for case_id, name in headings:
            catalog.append(
                {
                    "path": relative,
                    "id": case_id,
                    "title": f"{case_id} · {name.strip()}",
                    "area": "IAW",
                    "unit": unit,
                    "level": "Casos",
                }
            )

    for path in sorted((ROOT / "IAW/03_Simulacros").glob("simulacro_*.md")):
        afegir_fitxer(catalog, path, "IAW", "Simulacros escritos", "Simulacro")

    catalog.sort(key=lambda x: (x["area"], x["path"], x.get("id", "")))
    output = ROOT / "catalogo.json"
    output.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Catálogo actualizado: {len(catalog)} recursos en {output}")


if __name__ == "__main__":
    main()
