#Los bucles te permiten repetir bloques de código múltiples veces. Aqui usare los bucles for y while

# Bucle for para iterar sobre un rango de números
for numero in range(1, 6):  # rango(1, 6) genera números del 1 al 5
    print(numero)

#WHILE
# Inicializamos una variable contador con el valor 5
contador = 4

# Definimos una condición: mientras 'contador' sea mayor que 0
while contador > 0:
    # Este bloque de código se ejecuta mientras la condición sea verdadera
    print("Contador:", contador)
    
    # Decrementamos el valor de 'contador' en 1 en cada iteración
    contador -= 1
# Cuando 'contador' alcanza el valor 0, la condición se vuelve falsa y el bucle termina
print("Cuenta atras terminada")


