# -*- coding: utf-8 -*-
# EXERCICI 15 · Velocitat de xarxa
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana megabits per segon i calcula megabytes per segon.
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

megabits = float(input("Introduce los megabits por segundo: "))

megabytes = megabits / 8

print(f"Los megabytes por segundo son {megabytes:.2f}")