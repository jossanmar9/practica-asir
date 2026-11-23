# -*- coding: utf-8 -*-
# EXERCICI 11 · Mitjana de notes
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana tres notes i calcula la mitjana amb decimals.
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

nota_1 = float(input("Introduce la primera nota: "))
nota_2 = float(input("Introduce la segunda nota: "))
nota_3 = float(input("Introduce la tercera nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(f"La media de notas es {media:.2f}")