# Ejercicio 16
#
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

# Escribe tu solución debajo:

vehiculo_1 = int(input("Escribe la velocidad: "))
vehiculo_2 = int(input("Escribe la velocidad: "))
distancia = int(input("Escribe la distancia: "))

diferencia = vehiculo_2 - vehiculo_1

tiempo_h = distancia / diferencia
tiempo_m = tiempo_h * 60

print("los vehículos se encontrarán en", int(tiempo_m), "minutos")