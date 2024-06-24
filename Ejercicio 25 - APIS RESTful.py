from flask import Flask, jsonify, request  # Importamos Flask para crear la aplicación web, jsonify para convertir datos a formato JSON y request para manejar solicitudes HTTP

app = Flask(__name__)  # Creamos una instancia de la clase Flask para nuestra aplicación web

# Definimos una ruta para obtener datos, usando el método GET de HTTP
@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    datos = {"nombre": "Juan", "edad": 30}  # Creamos un diccionario con datos de ejemplo
    return jsonify(datos)  # Convertimos el diccionario a JSON y lo retornamos como respuesta

# Definimos una ruta para recibir datos, usando el método POST de HTTP
@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    nuevo_dato = request.json  # Obtenemos los datos enviados en la solicitud HTTP en formato JSON
    return jsonify({"mensaje": "Dato recibido", "dato": nuevo_dato}), 201  # Retornamos una respuesta JSON con el dato recibido y un código de estado 201 (creado)

# Ejecutamos la aplicación solo si este archivo se ejecuta directamente (no si es importado como módulo)
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutamos la aplicación Flask en modo debug, lo que proporciona información detallada de errores y recarga automática
