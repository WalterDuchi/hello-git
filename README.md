# Renombrar grupos de archivos en local a partir de la fecha más antigua de sus metadatos 
## Renombrar archivos con la fecha más antigua

Este script de Python te permite renombrar archivos en un directorio dado utilizando la fecha más antigua entre la fecha de creación, la fecha de modificación y la fecha de "Date Taken" (si está disponible en los metadatos EXIF de las imágenes).

### Requisitos

- Python 3.x instalado en tu sistema.
- La biblioteca `exifread` debe estar instalada. Puedes instalarla ejecutando el siguiente comando en tu terminal o símbolo del sistema:
    `pip install exifread`
    
### Cómo usar

1. Clona o descarga el archivo `renombrarConFecha.py` en tu sistema.
2. Abre una terminal o símbolo del sistema.
3. Navega hasta el directorio donde guardaste el archivo `renombrarConFecha.py`.
4. Ejecuta el script utilizando Python:
    `python renombrarConFecha.py`
5. El script buscará archivos en el directorio especificado y los renombrará con el formato "año-mes-día hora-minuto-segundo.extensión", utilizando la fecha más antigua entre la fecha de creación, la fecha de modificación y la fecha de "Date Taken".
6. Si hay archivos con nombres duplicados después de haber sido renombrados, el script agregará un número entre paréntesis para evitar conflictos de nombres.

¡Eso es todo! Ahora tus archivos estarán ordenados según sus fechas más antiguas.