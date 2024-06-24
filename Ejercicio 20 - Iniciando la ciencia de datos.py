import pandas as pd  # Importamos pandas para manipulación de datos
import matplotlib.pyplot as plt  # Importamos matplotlib para graficar
import seaborn as sns  # Importamos seaborn para graficar

# Cargamos un conjunto de datos de ejemplo
df = sns.load_dataset("iris")

# Mostramos los primeros registros del DataFrame
print(df.head())

# Creamos un gráfico de dispersión
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species")
plt.title("Gráfico de Dispersión de Iris")  # Añadimos un título al gráfico
plt.show()  # Mostramos el gráfico
