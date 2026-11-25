# Ejercicio 15
#
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

# Escribe tu solución debajo:

variable_a = int(input("Escribe el número: "))
variable_b = int(input("Escribe el número: "))

print("Variable A: ", variable_a)
print("Variable B: ", variable_b)

variable_c = variable_a
variable_a = variable_b
variable_b = variable_c

print("Variable A: ", variable_a)
print("Variable B: ", variable_b)