# Definimos una lista de números
# Las listas son colecciones ordenadas y mutables (se pueden modificar)
numeros = [1, 2, 3, 4, 5]
# Definimos una lista de nombres
nombres = ["Ana", "Juan", "Maria"]

# Definimos una tupla de coordenadas (x, y)
# Las tuplas son colecciones ordenadas e inmutables (no se pueden modificar después de ser creadas)
punto = (10, 20)
# Definimos una tupla de colores
colores = ("rojo", "verde", "azul")

# Accedemos al primer elemento de la lista de números
print("Primer elemento de la lista:", numeros[0])
# Accedemos al segundo elemento de la tupla de colores
print("Segundo elemento de la tupla:", colores[1])

# Actualizamos el tercer elemento de la lista de números
numeros[2] = 30
print("Lista actualizada:", numeros)
# Agregamos un elemento al final de la lista de números
numeros.append(6)#Append permite agregar un elemento al final de la lista
# Eliminamos el elemento "Ana" de la lista de nombres
nombres.remove("Ana")#Remove sirve para eliminar un elemento de una lista
# Mostramos la lista de nombres actualizada
print("Nombres despues de eliminar 'Ana':", nombres)

# Diferencias clave entre listas y tuplas:
# 1. Mutabilidad:
# Las listas son mutables: se pueden modificar, añadir o eliminar elementos después de su creación.
# Las tuplas son inmutables: no se pueden cambiar, añadir o eliminar elementos después de su creación.

# 2. Uso:
# Las listas se utilizan cuando necesitamos una colección de elementos que pueda cambiar (añadir o eliminar elementos).
# Las tuplas se utilizan cuando necesitamos una colección de elementos que no cambiará a lo largo de la ejecución del programa.