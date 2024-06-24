import pandas as pd

# Crear un DataFrame desde un diccionario
datos = {
    "Nombre": ["Juan", "María", "Pedro"],
    "Edad": [30, 25, 28],
    "Ciudad": ["México", "Madrid", "Lima"]
}

df = pd.DataFrame(datos)  # Creamos un DataFrame de Pandas
print(df)  # Mostramos el DataFrame

# Filtrar datos mayores de 25 años
mayores_de_25 = df[df['Edad'] > 25]
print("\nPersonas mayores de 25 años:")
print(mayores_de_25)
