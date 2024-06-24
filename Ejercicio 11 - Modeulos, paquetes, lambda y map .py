# Ejemplo de importación de módulos
import math

# Usamos funciones del módulo math
print("Valor de pi:", math.pi)  # Accedemos al valor de pi
print("Raiz cuadrada de 16:", math.sqrt(16))  # Calculamos la raíz cuadrada de 16


# Función lambda para calcular el cuadrado de un número
cuadrado = lambda x: x ** 2
print("Cuadrado de 5:", cuadrado(5))  # Llamamos a la función lambda con argumento 5

# Función map() para aplicar una función a una lista
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))  # Calculamos el cuadrado de cada número en la lista
print("Cuadrados de los números:", cuadrados)  # Mostramos la lista de cuadrados
