# El manejo de excepciones en Python se utiliza para gestionar errores que pueden 
# ocurrir durante la ejecución de un programa. Permite que el programa responda a 
# errores de una manera controlada y evite que el programa termine abruptamente.
#try: Contiene el código que puede generar una excepción.
#except: Contiene el código que se ejecuta si ocurre una excepción.
#finally: Contiene el código que se ejecuta siempre, haya o no ocurrido una excepción. 

# Ejemplo de manejo de excepciones
try:
    # Intentamos realizar una división por cero
    resultado = 10 / 0
except ZeroDivisionError:  # Capturamos la excepción de división por cero
    print("No se puede dividir entre cero.")
finally:
    # El bloque finally se ejecuta siempre, haya o no excepción
    print("Este bloque se ejecuta siempre, haya o no excepción.")
