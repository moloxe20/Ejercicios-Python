import concurrent.futures
import time

# Función para simular una tarea costosa
def tarea_costosa(segundos):
    print(f"Iniciando tarea que toma {segundos} segundo(s)...")
    time.sleep(segundos)
    return f"Tarea completada en {segundos} segundo(s)."

# Usar ThreadPoolExecutor para ejecutar varias tareas concurrentemente
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Lanzar múltiples tareas y obtener los resultados
    resultados = [executor.submit(tarea_costosa, i) for i in range(1, 4)]

    for resultado in concurrent.futures.as_completed(resultados):
        print(resultado.result())

print("Todas las tareas han sido completadas.")
