# -*- coding: utf-8 -*-
# EXERCICI 16 · Operacions amb enters
# Bloc: UT1 · Variables, tipus i conversions
#
# ENUNCIAT
# Demana dos enters i mostra suma, producte, divisió entera i residu.
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

numero_1 = int(input("Introduce el primer número: "))
numero_2 = int(input("Introduce el segundo número: "))

suma = numero_1 + numero_2
producto = numero_1 * numero_2
division = numero_1 // numero_2
resto = numero_1 % numero_2

print(f"El resultado de la suma de {numero_1} y {numero_2} es {suma}, de su multiplicación es {producto}, el de su división es {division} con un resto de {resto}")