# Ejercicio 5: Fecha desde nombre de backup
#
# Pista: find, [:] y replace
#
# Dado un nombre de archivo llamado 'backup_2025_09_03.tar.gz' extrae la fecha en formato '03-09-2025' (puedes extraer el año, mes y día y luego unirlos con guiones) e imprímela. Luego cambia a '.zip' el nombre del archivo original y muéstralo.

# Escribe tu solución debajo:

archivo = "backup_2025_09_03.tar.gz"

primero = archivo.find("_")
segundo = archivo.find("_", primero + 1)
tercero = archivo.find("_", segundo + 1)
punto = archivo.find(".")

anio = archivo[primero + 1:segundo]
mes = archivo[segundo + 1:tercero]
dia = archivo[tercero + 1:punto]

fecha_inversa = dia + "-" + mes + "-" + anio
archivo_zip = archivo.replace("tar.gz", "zip")

print(fecha_inversa)
print(archivo_zip)