# Ejercicio 17
#
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# Escribe tu solución debajo:

hora_salida = int(input("Hora de salida: "))
minutos_salida = int(input("Minutos de salida: "))
segundos_salida = int(input("Segundos de salida: "))

viaje = int(input("Segundos que ha durado el viaje: "))

total_segundos = (hora_salida * 3600) + (minutos_salida * 60) + segundos_salida

total_viaje = total_segundos + viaje

hora_llegada = total_viaje // 3600
resto = total_viaje % 3600
minutos_llegada = resto // 60
segundos_llegada = resto % 60

print(f"La hora de llegada ha sido las {hora_llegada}:{minutos_llegada}:{segundos_llegada}")