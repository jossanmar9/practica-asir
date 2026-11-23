# -*- coding: utf-8 -*-
# EXERCICI 02 · Edat del sistema
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana un any d'instal·lació i calcula els anys transcorreguts respecte a 2026.
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

any = int(input("Año de instalación: "))

diferencia = 2026 - any

print("El programa se instaló hace", diferencia, "años")