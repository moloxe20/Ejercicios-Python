import csv

# Escribir datos en un archivo CSV
datos = [
    {"nombre": "Armando", "edad": 30, "ciudad": "Lima"},
    {"nombre": "Juana", "edad": 25, "ciudad": "Cuzco"}
]

with open("datos.csv", "w", newline="") as archivo_csv:
    campos = ["nombre", "edad", "ciudad"]
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    
    escritor_csv.writeheader()  # Escribimos los encabezados
    for persona in datos:
        escritor_csv.writerow(persona)  # Escribimos cada fila

print("Se han escrito los datos en 'datos.csv'.")

#Es una poderosa biblioteca de Python utilizada 
# para el análisis y manipulación de datos. 
# Se importa convencionalmente bajo el alias pd para facilitar su uso.

import pandas as pd

# Crear un DataFrame desde un diccionario
datos = {
    "Nombre": ["German", "Diego", "Julio"],
    "Edad": [30, 25, 28],
    "Ciudad": ["Cuzco", "Huancayo", "Lima"]
}

df = pd.DataFrame(datos)  # Creamos un DataFrame de Pandas
print(df)  # Mostramos el DataFrame
