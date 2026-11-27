# Ejercicio 1¶
#
# Alerta por uso de disco
# Pistas: shutil.disk_usage, sys.argv
# Pide (por argumento) un umbral de uso de disco en porcentaje (por ejemplo, 85).
# Obtén el uso de disco de la partición raíz y muestra:
# - "ALERTA" si el porcentaje es mayor o igual que el umbral
# - "OK" en caso contrario.

# Escribe tu solución debajo:

import shutil
import sys

umbral = float(sys.argv[1])

total, usado, libre = shutil.disk_usage("/")

porcentaje = usado / total * 100

if porcentaje >= umbral:
    print("ALERTA")
else:
    print("OK")
