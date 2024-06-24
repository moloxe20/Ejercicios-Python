# Leer un archivo
with open("archivo.txt", "r") as archivo:  # Abrimos el archivo en modo lectura
    contenido = archivo.read()  # Leemos todo el contenido del archivo
    print("Contenido del archivo:")
    print(contenido)

# Escribir en un archivo
with open("nuevo_archivo.txt", "w") as archivo:  # Abrimos el archivo en modo escritura
    archivo.write("Hola, este es un nuevo archivo.")  # Escribimos una línea en el archivo
    archivo.write("\nSegunda línea del archivo.")  # Escribimos otra línea en el archivo
    print("Se ha escrito en el archivo.")
