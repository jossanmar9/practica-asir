# Ejercicio 5
#
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

# Escribe tu solución debajo:

usuario = input("Usuario: ")
contrasenya = input("Contraseña:")

if usuario == "pepe" and contrasenya == "asdasd":
    print("Has entrado al sistema")
else:
    print("Usuario o contraseña incorrecto")