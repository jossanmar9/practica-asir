# Ejercicio 9
#
# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

# Escribe tu solución debajo:

compra = float(input("Total compra: "))

descuento = compra * 0.15

pago = compra - descuento

print(pago, "€")
