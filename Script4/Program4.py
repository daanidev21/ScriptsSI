import os
import cv2
from pyzbar.pyzbar import decode

# Method to decode the barcode
def BarcodeReader(image_path):
    # Read the image in numpy array using cv2
    img = cv2.imread(image_path)
    
    # Decode the barcode image
    detectedBarcodes = decode(img)
    
    # If not detected then print the message
    if not detectedBarcodes:
        print(f"Barcode Not Detected or the barcode is blank/corrupted in {os.path.basename(image_path)}!")
    else:
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
            
            # Put the rectangle in image using cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)
            
            if barcode.data:
                # Print the barcode data (assumed to be the ID)
                barcode_data = barcode.data.decode('utf-8')
                print(f"Filename: {os.path.basename(image_path)}")
                print(f"Barcode ID: {barcode_data}")
                print(f"Barcode Type: {barcode.type}")
                print("Pulse una tecla para finalizar")
                
        # Display the image
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
	# Directorio proporcionado por el usuario para analizar los códigos de barras
	directorio = input("Inserte el directorio con el/los códigos de barras: ")
	
	# Comprobar el directorio
	if not os.path.isdir(directorio):
		print(f"El directorio {directorio} no existe.")
	else:
		# Preguntar por la imagen a analizar
		nombre_imagen = input("Inserte el nombre del archivo de imagen (incluyendo la extensión): ")
		
		# Comprobar si el archivo de imagen existe en el directorio
		image_path = os.path.join(directorio, nombre_imagen)
		if not os.path.isfile(image_path):
			print(f"No se encontró el archivo {nombre_imagen} en el directorio {directorio}.")
		else:
			# Procesar el archivo de imagen
			BarcodeReader(image_path)
