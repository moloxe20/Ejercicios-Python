#pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # Importamos la función para dividir los datos en entrenamiento y prueba
from sklearn.ensemble import RandomForestClassifier  # Importamos el clasificador RandomForest
from sklearn.metrics import accuracy_score  # Importamos la función para calcular la precisión

# Cargamos el conjunto de datos de Iris
iris = load_iris()
X = iris.data  # Asignamos las características a X
y = iris.target  # Asignamos las etiquetas a y

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creamos y entrenamos un modelo de Random Forest
modelo = RandomForestClassifier(n_estimators=100)  # Creamos el modelo con 100 árboles
modelo.fit(X_train, y_train)  # Entrenamos el modelo con los datos de entrenamiento

# Hacemos predicciones en el conjunto de prueba
predicciones = modelo.predict(X_test)

# Calculamos la precisión del modelo
precision = accuracy_score(y_test, predicciones)
print("Precisión del modelo:", precision)  # Imprimimos la precisión
