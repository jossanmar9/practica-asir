# Ejercicio 8
#
# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

# Escribe tu solución debajo:

sueldo_base = float(input("Sueldo base:"))
venta_1 = float(input("Venta 1: "))
venta_2 = float(input("Venta 2: "))
venta_3 = float(input("Venta 3: "))

comision= (venta_2 + venta_2 + venta_3) * 0.10

sueldo = sueldo_base + comision

print(sueldo, "€")
