# Ejercicio 2¶
#
# Turno de backup según hora 
# Pistas: datetime
# Obtén la hora actual y muestra:
# - "Backup de mañana" si hora < 12
# - "Backup de tarde" si 12 <= hora < 20
# - "Backup nocturno" si hora >= 20

# Escribe tu solución debajo:

from datetime import datetime

hora = datetime.now().hour

if hora < 12:
    print("Backup de mañana")
elif hora <= 12 and hora < 20:
    print("Backup de tarde")
else:
    print("Backup nocturno")