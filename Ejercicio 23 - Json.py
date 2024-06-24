import json  # Importamos el módulo json para trabajar con JSON

# Definimos un diccionario
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Peru"
}

# Convertimos el diccionario a una cadena JSON
json_datos = json.dumps(datos)
print("Datos en formato JSON:", json_datos)  # Imprimimos la cadena JSON

# Convertimos una cadena JSON a un diccionario
diccionario_datos = json.loads(json_datos)
print("Datos convertidos de JSON a diccionario:", diccionario_datos)  # Imprimimos el diccionario
