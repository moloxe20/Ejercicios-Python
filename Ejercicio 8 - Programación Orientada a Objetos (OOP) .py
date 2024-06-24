# Definimos una clase llamada 'Persona'
class Persona:
    # El método __init__ se llama cuando se crea una instancia de la clase
    # El método __init__ inicializa los atributos de la clase
    def __init__(self, nombre, edad):
        # Atributos de la clase - SELF: se utiliza como nombre para el primer parámetro de un método en una clase.
        self.nombre = nombre  # 'self.nombre' es un atributo de la clase 'Persona'
        self.edad = edad      # 'self.edad' es otro atributo de la clase 'Persona'
    
    # Método para saludar
    # Este método imprime un saludo utilizando el atributo 'nombre'
    def saludar(self):
        print("Hola, mi nombre es", self.nombre, " y tengo ", self.edad ," años.")

# Creamos una instancia de la clase Persona
# 'persona1' es un objeto de la clase 'Persona' con nombre "María" y edad 30
persona1 = Persona("Maria", 30)
# 'persona2' es otro objeto de la clase 'Persona' con nombre "Pedro" y edad 25
persona2 = Persona("Pedro", 25)
# Llamamos al método saludar de cada instancia
# 'persona1.saludar()' llama al método 'saludar' para el objeto 'persona1'
persona1.saludar()
# 'persona2.saludar()' llama al método 'saludar' para el objeto 'persona2'
persona2.saludar()

#Abstracción
# Definición de la clase abstracta Animal
#Es el proceso de identificar las características esenciales de un objeto y eliminar los detalles innecesarios.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass  # Este método será implementado en las clases hijas

# Clase perro hereda de la clase Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

# Clase gato hereda de la clase Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

# Creación de objetos de tipo Perro y Gato
mi_perro = Perro("Bobby")
mi_gato = Gato("Pelusa")

# Uso del método hacer_sonido que es abstracto en Animal pero implementado en Perro y Gato
print(mi_perro.nombre + ": " + mi_perro.hacer_sonido())
print(mi_gato.nombre + ": " + mi_gato.hacer_sonido())
# la clase Animal define un método hacer_sonido que es implementado de manera 
# diferente en las clases hijas (Perro y Gato), permitiendo que cada instancia 
# de animal realice sonidos específicos.


#Encapsulamiento

# es el ocultamiento del estado interno de un objeto y el 
# requerimiento de que todos los cambios en el estado del 
# objeto se realicen a través de métodos definidos.

# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.__modelo = modelo  # Atributo privado
    def get_modelo(self):
        return self.__modelo  # Método para acceder al atributo privado
    def set_modelo(self, modelo):
        self.__modelo = modelo  # Método para actualizar el atributo privado
# Creación de un objeto de tipo Vehiculo
mi_auto = Vehiculo("Toyota", "Corolla")
# Acceso al atributo público
print("Marca:", mi_auto.marca)
# Acceso al atributo privado a través de un método
print("Modelo:", mi_auto.get_modelo())
# Actualización del atributo privado a través de un método
mi_auto.set_modelo("Camry")
print("Modelo actualizado:", mi_auto.get_modelo())
# a clase Vehiculo oculta el atributo __modelo utilizando 
# métodos públicos (get_modelo() y set_modelo()), lo que 
# controla cómo se accede y modifica ese atributo.


#Herencia
# permite que una clase (subclase) herede los métodos 
# y atributos de otra clase (superclase), promoviendo la reutilización del código.
class Persona:# Definición de la clase Persona (superclase)
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
#
# Definición de la clase Estudiante (subclase que hereda de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)  # Llamada al constructor de la superclase
        self.curso = curso

    def saludar(self):  # Polimorfismo: método saludar sobrescrito
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio en el curso {self.curso}."

# Creación de objetos de tipo Persona y Estudiante
persona1 = Persona("Luis", 30)
estudiante1 = Estudiante("Maria", 25, "Python")

# Uso del método saludar de la clase Persona
print(persona1.saludar())

# Uso del método saludar de la clase Estudiante (polimorfismo)
print(estudiante1.saludar())
#La clase Estudiante hereda atributos y métodos de la clase Persona, 
# extendiendo su funcionalidad al añadir el atributo curso y 
# sobrescribiendo el método saludar para adaptarlo al contexto de un estudiante.




#Polimorfismo permite que objetos de distintas clases respondan al 
# mismo mensaje (método) de manera diferente.
# Definición de la clase Figura (superclase)
class Figura:
    def area(self):
        pass  # Método abstracto que será implementado en las clases hijas

# Definición de la clase Rectangulo (subclase)
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):  # Implementación del método área para Rectángulo
        return self.base * self.altura

# Definición de la clase Circulo (subclase)
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):  # Implementación del método área para Círculo
        return 3.14159 * self.radio ** 2

# Creación de objetos de tipo Rectangulo y Circulo
mi_rectangulo = Rectangulo(5, 10)
mi_circulo = Circulo(7)

# Uso del método área (polimorfismo)
print("Área del rectángulo:", mi_rectangulo.area())
print("Área del círculo:", mi_circulo.area())

#las clases Rectangulo y Circulo heredan de Figura y cada una 
# implementa su propio método area, respondiendo al mismo mensaje 
# (area()) de manera diferente según el tipo de figura.

