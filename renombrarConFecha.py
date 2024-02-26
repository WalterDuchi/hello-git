# Importar el módulo os para interactuar con el sistema operativo
import os
# Importar la clase datetime del módulo datetime para trabajar con fechas y horas
from datetime import datetime
# Importar el módulo exifread para leer los metadatos EXIF de las imágenes
import exifread

# Definir la ruta del directorio donde se encuentran los archivos
directorio = r'C:\Users\Walter Duchi\OneDrive - Universidad de Guayaquil\Fotos Celular'

# Obtener la lista de archivos en el directorio especificado
archivos = os.listdir(directorio)

# Inicializar un diccionario para almacenar el contador de nombres duplicados
contador = {}

# Iterar sobre cada archivo en la lista de archivos
for archivo in archivos:
    # Obtener la ruta completa del archivo concatenando el directorio y el nombre del archivo
    ruta_completa = os.path.join(directorio, archivo)
    
    # Obtener la fecha de creación del archivo a partir de la marca de tiempo de creación del archivo
    fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_completa))
    
    # Obtener la fecha de modificación del archivo a partir de la marca de tiempo de modificación del archivo
    fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa))
    
    # Intentar obtener la fecha de "Date Taken" del archivo a partir de los metadatos EXIF
    try:
        with open(ruta_completa, 'rb') as f:
            # Procesar los metadatos EXIF del archivo y obtener la fecha original de la imagen
            tags = exifread.process_file(f, details=False)
            fecha_taken = datetime.strptime(str(tags['EXIF DateTimeOriginal']), '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        # Si no se puede obtener la fecha de "Date Taken", asignar None a fecha_taken
        fecha_taken = None
    
    # Determinar la fecha más antigua entre la fecha de creación, la fecha de modificación y la fecha de "Date Taken"
    fechas = [fecha_creacion, fecha_modificacion]
    if fecha_taken:
        fechas.append(fecha_taken)
    fecha_antigua = min(fechas)
    
    # Formatear la fecha en el formato deseado para el nuevo nombre de archivo
    nuevo_nombre = fecha_antigua.strftime('%Y-%m-%d %H-%M-%S') + os.path.splitext(archivo)[1]
    
    # Verificar si el nuevo nombre ya existe en el directorio
    while os.path.exists(os.path.join(directorio, nuevo_nombre)):
        # Si el nuevo nombre ya existe, incrementar el contador para evitar nombres duplicados
        contador[nuevo_nombre] = contador.get(nuevo_nombre, 0) + 1
        nuevo_nombre = fecha_antigua.strftime('%Y-%m-%d %H-%M-%S') + f" ({contador[nuevo_nombre]})" + os.path.splitext(archivo)[1]
    
    # Renombrar el archivo con el nuevo nombre generado
    os.rename(ruta_completa, os.path.join(directorio, nuevo_nombre))
