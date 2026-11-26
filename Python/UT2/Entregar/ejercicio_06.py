# Ejercicio 6: Partes de un email institucional
#
# Pista: index/find y [:]
#
# Dado el email 'admin.redes@centro.edu', extrae el usuario (antes de '@'), el dominio (entre '@' y primer '.') y el tld (después del '.'). No uses bucles.

# Escribe tu solución debajo:

mail = "admin.redes@centro.edu"

punto_1 = mail.find(".")
arroba = mail.find("@")
punto_2 = mail.find(".", punto_1 + 1)

usuario = mail[:arroba]
dominio = mail[arroba + 1: punto_2]
tld = mail[punto_2 + 1:]

print(usuario)
print(dominio)
print(tld)