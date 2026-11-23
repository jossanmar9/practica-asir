# -*- coding: utf-8 -*-
# EXERCICI 05 · Preu amb IVA
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana base imposable i calcula el total amb un IVA del 21%.
#
# REQUISITS
# - Resol el problema amb els conceptes d'este bloc.
# - Utilitza noms de variables descriptius.
# - Mostra resultats clars i comprensibles.
# - No inclogues dades personals reals ni modifiques fitxers del sistema.
#
# Comprovacions suggerides:
# - Prova almenys un cas normal i un cas límit.
# - Comprova el format exacte de la sortida.
# - Si l'enunciat demana validació, prova també una entrada incorrecta.
# - No utilitzes funcions avançades per evitar practicar el concepte central.
# ESCRIU LA TEUA SOLUCIÓ A PARTIR D'ACÍ:

base = float(input("Introduce la base imponible: "))
IVA = 0.21

impuesto = base * IVA

precio = base + impuesto

print(f"El precio con IVA es {precio:.2f} €")