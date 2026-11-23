# -*- coding: utf-8 -*-
# EXERCICI 03 · Inventari de perifèrics
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana quantitats de teclats, ratolins i monitors i mostra el total.
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

teclados = int(input("Cuantos teclados hay: "))
ratones = int(input("Cuantos ratones hay: "))
monitores = int(input("Cuantos monitores hay: "))

suma = teclados + ratones + monitores

print("En total hay", suma, "perifericos")