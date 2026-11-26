# Ejercicio 8: Username a partir de nombre y apellido
#
# Pista: librería string, librería random, strip, replace, [:]
#
# Vamos a generar un nombre de usuario. Dado un nombre=' Ana ' y un apellido=' López ' genera su usuario con las primeras 3 letras del nombre + las 3 primeras letras de su apellido + dos dígitos aleatorios. Ten en cuenta que el nombre de usuario no puede tener vocales con acentos. Suponemos que sólo existen acentos en español.

# Escribe tu solución debajo:

import string
import random

nombre = " Ana "
apellido = " López"
digitos = string.digits

nombre_l = nombre.strip()
apellido_1 = apellido.strip()

acento = apellido_1.replace("ó", "o")

usuario = nombre_l[0:3] + acento[0:3] + random.choice(digitos) + random.choice(digitos)

print(usuario)