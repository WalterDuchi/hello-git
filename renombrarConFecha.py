import os
from datetime import datetime
import exifread

# Directorio de origen
directorio = r'C:\Users\Walter Duchi\Pictures\prueba'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Diccionario para almacenar el contador de nombres duplicados
contador = {}

# Recorrer cada archivo
for archivo in archivos:
    # Obtener la ruta completa del archivo
    ruta_completa = os.path.join(directorio, archivo)
    
    # Obtener la fecha de creación del archivo
    fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa))
    
    # Intentar obtener la fecha de "Date Taken" del archivo
    try:
        with open(ruta_completa, 'rb') as f:
            tags = exifread.process_file(f, details=False)
            fecha_tomada = datetime.strptime(str(tags['EXIF DateTimeOriginal']), '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        # Si no se puede obtener la fecha de "Date Taken", usar la fecha de creación del archivo
        print(f"No se pudo obtener la fecha de 'Date Taken' para {archivo}. Se usará la fecha de creación.")
        fecha_tomada = fecha_creacion
    
    # Formatear la fecha como deseas para el nuevo nombre de archivo
    nuevo_nombre = fecha_tomada.strftime('%m-%d-%Y %H-%M-%S') + os.path.splitext(archivo)[1]
    
    # Verificar si el nuevo nombre ya existe
    while os.path.exists(os.path.join(directorio, nuevo_nombre)):
        # Si el nuevo nombre ya existe, agregar un contador al nombre del archivo
        contador[nuevo_nombre] = contador.get(nuevo_nombre, 0) + 1
        nuevo_nombre = fecha_tomada.strftime('%m-%d-%Y %H-%M-%S') + f" ({contador[nuevo_nombre]})" + os.path.splitext(archivo)[1]
    
    # Renombrar el archivo con el nuevo nombre
    os.rename(ruta_completa, os.path.join(directorio, nuevo_nombre))
