import sqlite3

# Conectar a una base de datos SQLite (o crearla si no existe)
conexion = sqlite3.connect("ejemplo.db")

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER
                )''')

# Insertar datos en la tabla
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 30))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("María", 25))

# Guardar cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Se ha creado la base de datos 'ejemplo.db' y se han insertado datos.")
