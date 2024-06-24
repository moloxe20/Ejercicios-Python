import matplotlib.pyplot as plt

# Datos para graficar
etiquetas = ['A', 'B', 'C']
valores = [20, 50, 30]

# Crear un gráfico de barras
plt.bar(etiquetas, valores, color='blue')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras')
plt.show()
