import requests  # Importamos la biblioteca requests para hacer peticiones HTTP

# Realizamos una petición GET a una API pública
respuesta = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Verificamos que la petición fue exitosa
if respuesta.status_code == 200:
    datos = respuesta.json()  # Convertimos la respuesta a un diccionario
    print("Datos recibidos:")
    print(datos)  # Imprimimos los datos recibidos
else:
    print("Error al hacer la petición:", respuesta.status_code)  # Imprimimos un mensaje de error si la petición falla
