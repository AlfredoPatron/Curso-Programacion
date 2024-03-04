from pathlib import Path

carpeta = Path('d:/alfre/Desktop/Alternativo')
archivo = carpeta / 'otro_archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

