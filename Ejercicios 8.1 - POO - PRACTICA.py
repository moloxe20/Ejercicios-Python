# Definición de la clase abstracta Empleado (abstracción)
class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.__salario_base = salario_base  # Encapsulamiento del salario base
    
    # Método getter para obtener el salario base
    def get_salario_base(self):
        return self.__salario_base
    
    # Método setter para actualizar el salario base
    def set_salario_base(self, nuevo_salario):
        self.__salario_base = nuevo_salario
    
    # Método abstracto para calcular el salario (será implementado en las clases hijas)
    def calcular_salario(self):
        pass

# Definición de la clase Desarrollador (herencia)
class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje_principal):
        super().__init__(nombre, salario_base)
        self.lenguaje_principal = lenguaje_principal
    
    # Implementación del método para calcular salario para desarrolladores
    def calcular_salario(self):
        return self.get_salario_base() + 5000  # Ejemplo simple de bono para desarrolladores

# Definición de la clase Gerente (herencia)
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, nivel):
        super().__init__(nombre, salario_base)
        self.nivel = nivel
    
    # Implementación del método para calcular salario para gerentes
    def calcular_salario(self):
        return self.get_salario_base() + (self.nivel * 1000)  # Ejemplo de bono según nivel

# Función para mostrar información del empleado
def mostrar_informacion(empleado):
    print(f"Nombre: {empleado.nombre}")
    print(f"Salario Base: S/{empleado.get_salario_base()}")
    print(f"Salario Total: S/{empleado.calcular_salario()}")
    print()

# Creación de objetos de tipo Desarrollador y Gerente
desarrollador1 = Desarrollador("Paquita", 60000, "Python")
gerente1 = Gerente("Paquito", 80000, 3)

# Mostrar información de los empleados utilizando polimorfismo
print("Informacion del Desarrollador:")
mostrar_informacion(desarrollador1)

print("Informacion del Gerente:")
mostrar_informacion(gerente1)
