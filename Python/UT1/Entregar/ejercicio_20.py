# Ejercicio 20
#
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos). Utiliza el operador %.

# Escribe tu solución debajo:

moneda_2 = int(input("Introduce el numero de monedas de 2 €: "))
moneda_1 = int(input("Introduce el numero de monedas de 1 €: "))
moneda_50 = int(input("Introduce el numero de monedas de 50 centimos: "))
moneda_20 = int(input("Introduce el numero de monedas de 20 centimos: "))
moneda_10 = int(input("Introduce el numero de monedas de 10 centimos: "))

centimos_totales = (moneda_2 * 200) + (moneda_1 * 100) + (moneda_50 * 50) + (moneda_20 * 20) + (moneda_10 * 10)

euros = centimos_totales // 100
centimos = centimos_totales % 100

print(f"Tenemos un total de {euros} euros y {centimos} centimos")