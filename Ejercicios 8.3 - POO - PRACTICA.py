class Libro:
    def __init__(self, titulo, autor, genero, disponibilidad):
        self.titulo = titulo    
        self.autor = autor
        self.genero = genero 
        self.__disponibilidad = disponibilidad
        
    def get_disponibilidad(self):
        return self.__disponibilidad
    
    def set_disponibilidad(self, nueva_disponibilidad):
        self.__disponibilidad = nueva_disponibilidad


class Usuario:
    def __init__(self, name, age, dni, limite):
        self.name = name
        self.age = age
        self.dni = dni
        self.__limite = limite
      
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, nuevo_limite):
        self.__limite = nuevo_limite


class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def realizar_prestamo(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        if libro.get_disponibilidad() > 0 and usuario.get_limite() > 0:
            prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
            self.prestamos.append(prestamo)
            libro.set_disponibilidad(libro.get_disponibilidad() - 1)
            usuario.set_limite(usuario.get_limite() - 1)
            print(f"Prestamo realizado: {libro.titulo} para {usuario.name}")
        else:
            print(f"No se pudo realizar el préstamo de {libro.titulo} para {usuario.name}.")
    
    def devolver_libro(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.libro == libro:
                self.prestamos.remove(prestamo)
                libro.set_disponibilidad(libro.get_disponibilidad() + 1)
                usuario.set_limite(usuario.get_limite() + 1)
                print(f"Devolución realizada: {libro.titulo} por {usuario.name}")
                return
        print(f"No se encontró el préstamo de {libro.titulo} por {usuario.name}.")
    
    def consultar_disponibilidad(self, libro):
        print(f"Disponibilidad de {libro.titulo}: {libro.get_disponibilidad()} unidades")
    
    def consultar_prestamos_usuario(self, usuario):
        print(f"Prestamos de {usuario.name}:")
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario:
                print(f"- {prestamo.libro.titulo} (Devolver antes del {prestamo.fecha_devolucion})")
        print()


# Ejemplo de uso
if __name__ == "__main__":
    # Creación de objetos Libro y Usuario
    libro1 = Libro("Python for Beginners", "John Smith", "Educational", 5)
    libro2 = Libro("The Art of Programming", "Jane Doe", "Technical", 3)
    
    usuario1 = Usuario("Alice", 25, "12345678A", 3)
    usuario2 = Usuario("Bob", 30, "87654321B", 2)
    
    # Creación de objeto Biblioteca
    biblioteca = Biblioteca()
    
    # Agregar libros y registrar usuarios en la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    
    # Realizar préstamos
    biblioteca.realizar_prestamo(usuario1, libro1, "2024-06-21", "2024-07-05")
    biblioteca.realizar_prestamo(usuario2, libro2, "2024-06-22", "2024-07-07")
    
    # Intentar préstamo de libro no disponible
    biblioteca.realizar_prestamo(usuario1, libro1, "2024-06-23", "2024-07-08")
    
    # Consultar préstamos y disponibilidad
    biblioteca.consultar_prestamos_usuario(usuario1)
    biblioteca.consultar_disponibilidad(libro1)
    
    # Devolver libro
    biblioteca.devolver_libro(usuario1, libro1)
    
    # Consultar préstamos después de devolución
    biblioteca.consultar_prestamos_usuario(usuario1)
    biblioteca.consultar_disponibilidad(libro1)
