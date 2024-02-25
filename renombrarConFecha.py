import os
from datetime import datetime
import exifread

# Directorio de origen
directorio = r'C:\Users\Walter Duchi\OneDrive - Universidad de Guayaquil\Fotos Celular'

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
    
    # Obtener la fecha de modificación del archivo
    fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa))
    
    # Intentar obtener la fecha de "Date Taken" del archivo
    try:
        with open(ruta_completa, 'rb') as f:
            tags = exifread.process_file(f, details=False)
            fecha_taken = datetime.strptime(str(tags['EXIF DateTimeOriginal']), '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        # Si no se puede obtener la fecha de "Date Taken", asignar None
        fecha_taken = None
    
    # Determinar la fecha más antigua entre la fecha de creación, fecha de modificación y fecha de "Date Taken"
    fechas = [fecha_creacion, fecha_modificacion]
    if fecha_taken:
        fechas.append(fecha_taken)
    fecha_antigua = min(fechas)
    
    # Formatear la fecha como deseas para el nuevo nombre de archivo
    nuevo_nombre = fecha_antigua.strftime('%Y-%m-%d %H-%M-%S') + os.path.splitext(archivo)[1]
    
    # Verificar si el nuevo nombre ya existe
    while os.path.exists(os.path.join(directorio, nuevo_nombre)):
        # Si el nuevo nombre ya existe, agregar un contador al nombre del archivo
        contador[nuevo_nombre] = contador.get(nuevo_nombre, 0) + 1
        nuevo_nombre = fecha_antigua.strftime('%Y-%m-%d %H-%M-%S') + f" ({contador[nuevo_nombre]})" + os.path.splitext(archivo)[1]
    
    # Renombrar el archivo con el nuevo nombre
    os.rename(ruta_completa, os.path.join(directorio, nuevo_nombre))
