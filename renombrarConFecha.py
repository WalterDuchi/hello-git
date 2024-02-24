import os
from datetime import datetime

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
    
    # Obtener la fecha de modificación del archivo
    fecha_modificacion = datetime.fromtimestamp(os.path.getmtime(ruta_completa))
    
    # Determinar la fecha más antigua entre la fecha de creación y la fecha de modificación
    fecha_antigua = min(fecha_creacion, fecha_modificacion)
    
    # Formatear la fecha como deseas para el nuevo nombre de archivo
    nuevo_nombre = fecha_antigua.strftime('%m-%d-%Y %H-%M-%S') + os.path.splitext(archivo)[1]
    
    # Verificar si el nuevo nombre ya existe
    while os.path.exists(os.path.join(directorio, nuevo_nombre)):
        # Si el nuevo nombre ya existe, agregar un contador al nombre del archivo
        contador[nuevo_nombre] = contador.get(nuevo_nombre, 0) + 1
        nuevo_nombre = fecha_antigua.strftime('%m-%d-%Y %H-%M-%S') + f" ({contador[nuevo_nombre]})" + os.path.splitext(archivo)[1]
    
    # Renombrar el archivo con el nuevo nombre
    os.rename(ruta_completa, os.path.join(directorio, nuevo_nombre))
