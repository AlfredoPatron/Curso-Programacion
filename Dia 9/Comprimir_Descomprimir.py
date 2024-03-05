#comprimir con zipfile
import zipfile

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()


#descomprimir con zipfile

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()

#--------------------------------------------
#comprimir con shutil
import shutil

carpeta_origen = 'C:\\Users\\Win10\\Desktop\\Carpeta_Superior'

archivo_destino = 'Todo_comprimido'

shutil.make_archive(archivo_destino, 'zip,', carpeta_origen)


#descomprimir con shutil

shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion Terminada', 'zip')
