# Un diccionario es una colección no ordenada de pares clave-valor.
# Cada clave en un diccionario debe ser única y se utiliza para acceder al valor correspondiente.
# Los diccionarios se definen utilizando llaves {} y los pares clave-valor se separan por dos puntos (:).
# Los valores pueden ser de cualquier tipo y no necesitan ser únicos.
# Los diccionarios son mutables, lo que significa que podemos añadir, cambiar o eliminar pares clave-valor después de su creación.


# Definimos un diccionario con información de una persona
persona = {
    "nombre": "Luis",
    "edad": 20,
    "ciudad": "Colombia"
}

# Accedemos al valor asociado a la clave "nombre"
print("Nombre de la persona:", persona["nombre"])

# Accedemos al valor asociado a la clave "edad"
print("Edad de la persona:", persona["edad"])

# Actualizamos el valor de la clave "edad"
persona["edad"] = 26
print("Edad actualizada:", persona["edad"])


if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario.")

# Obtener todas las claves del diccionario
print("Claves del diccionario:", persona.keys())

# Obtener todos los valores del diccionario
print("Valores del diccionario:", persona.values())

# Obtener todos los pares clave-valor del diccionario
print("Pares clave-valor del diccionario:", persona.items())

