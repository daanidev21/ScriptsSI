import os
import shutil

"""Programa para organizar archivos en una carpeta. El programa tiene que tener una lista con varias opciones como mp4, png, doc... y debe creear carpetas con esos nombres y mover los archivos con esas extensiones dentro de esas carpetas."""

extensiones = ["png","jpg","doc","pdf", "txt", "avif", "avi", "mp3", "py", "java"]

def organizar_archivos():

	carpeta_actual = os.getcwd()

	for extension in extensiones:
		carpeta_nueva = os.path.join(carpeta_actual, extension)
		if not os.path.exists(carpeta_nueva):
			os.makedirs(carpeta_nueva)
			
	for archivo in os.listdir(carpeta_actual):
		ruta_origen = os.path.join(carpeta_actual, archivo)
		if os.path.isfile(ruta_origen):  # Verifica que sea un archivo
			for extension in extensiones:
				if archivo.endswith(f".{extension}"):
					ruta_destino = os.path.join(carpeta_actual, extension, archivo)
					shutil.move(ruta_origen, ruta_destino)
					print(f"moviendo {archivo} a {os.path.join(carpeta_actual, extension)}")
					
organizar_archivos()
