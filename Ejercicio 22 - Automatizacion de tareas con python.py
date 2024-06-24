import os  # Importamos el módulo os para operaciones del sistema
import shutil  # Importamos shutil para operaciones de archivos

# Crear un directorio
os.makedirs("nuevo_directorio", exist_ok=True)  # Creamos un directorio si no existe
print("Directorio creado.")  # Imprimimos un mensaje

# Verificar si el archivo existe antes de moverlo
if os.path.exists("archivo.txt"):
    # Mover un archivo a otro directorio
    shutil.move("archivo.txt", "nuevo_directorio/archivo.txt")  # Movemos un archivo al nuevo directorio
    print("Archivo movido.")  # Imprimimos un mensaje

    # Renombrar un archivo
    os.rename("nuevo_directorio/archivo.txt", "nuevo_directorio/archivo_renombrado.txt")  # Renombramos el archivo
    print("Archivo renombrado.")  # Imprimimos un mensaje
else:
    print("El archivo 'archivo.txt' no existe.")  # Imprimimos un mensaje si el archivo no existe

