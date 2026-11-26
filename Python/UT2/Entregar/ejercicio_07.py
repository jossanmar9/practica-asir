# Ejercicio 7: Password con patrón simple
#
# Pista: librería string, librería random
#
# Genera una contraseña de 10 caracteres: 4 letras + 4 dígitos + 2 símbolos de los siguientes '!#$%&*'. Sin bucles ni condicionales. Utiliza la librería string para obtener las letras y los dígitos. Utiliza la librería random para seleccionar aleatoriamente un elemento de los anteriores (de las letras, de los números y de los símbolos especiales).

# Escribe tu solución debajo:

import string
import random

letras = string.ascii_letters
digitos = string.digits
simbolos = "!#$%&*"

a = random.choice(letras)
b = random.choice(letras)
c = random.choice(letras)
d = random.choice(letras)

e = random.choice(digitos)
f = random.choice(digitos)
g = random.choice(digitos)
h = random.choice(digitos)

i = random.choice(simbolos)
j = random.choice(simbolos)

password = a + b + c + d + e + f + g + h + i + j
print("Password generada: ", password)
