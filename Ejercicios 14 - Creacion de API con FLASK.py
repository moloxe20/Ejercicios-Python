#Importamos las clases Flask y jsonify desde el módulo flask. 
# Flask es la clase principal que usamos para crear la aplicación web, y 
# jsonify es una función que convierte diccionarios de Python en respuestas JSON válidas.
from flask import Flask, jsonify

# Creamos una instancia de la clase Flask y le asignamos el nombre del módulo actual (__name__)
app = Flask(__name__)

# Definimos una ruta '/saludo/<nombre>' que acepta un parámetro de ruta llamado 'nombre'
# y define una función 'saludar' que devuelve un mensaje JSON con un saludo personalizado.
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return jsonify({'mensaje': 'Hola, ' + nombre + '!'})

# Si este archivo es ejecutado directamente (es decir, no importado como módulo),
# entonces ejecutamos la aplicación Flask en modo de depuración (debug) en el puerto 5000.
if __name__ == '__main__':
    app.run(debug=True)

