# Definimos una función llamada 'decorador' que recibe como parámetro otra función 'funcion'
def decorador(funcion):
    # Definimos una función interna llamada 'wrapper' que será la función de envoltura
    def wrapper():
        print("Antes de llamar a la función.")  # Imprimimos un mensaje antes de llamar a la función original
        funcion()  # Llamamos a la función original que fue pasada como parámetro
        print("Después de llamar a la función.")  # Imprimimos un mensaje después de llamar a la función original
    return wrapper  # Devolvemos la función de envoltura 'wrapper'

# Usamos el decorador '@' para aplicar el decorador 'decorador' a la función 'funcion_a_decorar'
@decorador
def funcion_a_decorar():
    print("¡Hola, mundo!")  # Esta es la función original que queremos decorar

# Llamamos a la función decorada 'funcion_a_decorar'
funcion_a_decorar()


# Ejemplo de manejo de excepciones con try-except
try:
    resultado = 10 / 0  # Intentamos dividir por cero
except ZeroDivisionError as e:  # Capturamos la excepción y la almacenamos en 'e'
    print("Error No se puede dividir entre cero:", e)  # Mostramos el mensaje de error

# Manejo de múltiples excepciones
try:
    lista = [1, 2, 3]
    print(lista[10])  # Intentamos acceder a un índice fuera de rango
except IndexError:  # Capturamos la excepción específica para índice fuera de rango
    print("Error Índice fuera de rango.")
except Exception as e:  # Capturamos cualquier otra excepción
    print("Ocurrió un error:", e)

# Bloque finally: siempre se ejecuta, haya o no excepciones
finally:
    print("Este bloque se ejecuta siempre, haya o no excepcion.")
