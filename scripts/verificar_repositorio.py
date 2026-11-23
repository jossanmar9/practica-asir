#!/usr/bin/env python3
"""Comprueba el catálogo, los bancos de preguntas y los enlaces de la portada."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    catalog = load_json("catalogo.json")
    keys = [e["path"] + ("#" + e["id"] if e.get("id") else "") for e in catalog]
    check(len(catalog) == 438, "El catálogo debe contener 438 recursos.")
    check(len(keys) == len(set(keys)), "Hay recursos duplicados en el catálogo.")
    for e in catalog:
        check((ROOT / e["path"]).is_file(), f"No existe el archivo: {e['path']}")
    print(f"Catálogo: {len(catalog)} recursos, sin rutas rotas.")

    for name, json_path, html_path, var, stop, question_key, options_key, answer_key, expected in (
        ("ASO", "ASO/banco_200_preguntas.json", "ASO/test_aso_ut1_ut2.html", "const bank=", ";let active=", "q", "a", "correct", 200),
        ("Python", "Python/test_teorico/preguntas.json", "Python/test_teorico/test_python_480_preguntas.html", "const BANK=", ";let exam", "q", "options", "answer", 480),
        ("IAW", "IAW/05_Test_HTML/banco_240_preguntas.json", "IAW/05_Test_HTML/test_IAW.html", "const bank=", ";let active=", "question", "options", "correct", 240),
    ):
        questions = load_json(json_path)
        check(len(questions) == expected, f"{name}: número incorrecto de preguntas.")
        for n, q in enumerate(questions, 1):
            options = q[options_key]
            check(len(options) == 4 and len(set(options)) == 4, f"{name}: opciones repetidas en pregunta {n}.")
            check(isinstance(q[answer_key], int) and 0 <= q[answer_key] < 4, f"{name}: respuesta inválida en pregunta {n}.")
        if name == "Python":
            check(len({q[question_key] for q in questions}) == expected, "Python: hay enunciados duplicados.")
        html = (ROOT / html_path).read_text(encoding="utf-8")
        begin = html.find(var)
        check(begin >= 0, f"{name}: falta el banco integrado en el HTML.")
        begin += len(var)
        end = html.find(stop, begin)
        check(end >= 0, f"{name}: no se encuentra el final del banco HTML.")
        embedded = json.loads(html[begin:end])
        check(embedded == questions, f"{name}: el HTML y el JSON no coinciden.")
        print(f"{name}: {expected} preguntas válidas y HTML/JSON sincronizados.")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    check('<html lang="es">' in html, "La portada debe estar en castellano.")
    for url in re.findall(r'href="([^"]+)"', html):
        if url.startswith(("https://", "http://", "#")) or url == "./":
            continue
        check((ROOT / url).is_file(), f"Enlace roto en la portada: {url}")
    print("Portada: idioma español y enlaces internos correctos.")
    print("Verificación completada.")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
