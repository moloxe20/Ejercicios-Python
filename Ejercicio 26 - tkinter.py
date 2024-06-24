import tkinter as tk  # Importamos el módulo tkinter para crear interfaces gráficas

# Creamos una ventana principal
ventana = tk.Tk()  # Instanciamos un objeto Tk, que representa la ventana principal
ventana.title("Mi Primera Ventana")  # Asignamos un título a la ventana

# Creamos una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")  # Creamos una etiqueta con un texto
etiqueta.pack()  # Añadimos la etiqueta a la ventana y la mostramos

# Creamos un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=lambda: print("Botón presionado"))  # Creamos un botón con un texto y una acción asociada
boton.pack()  # Añadimos el botón a la ventana y lo mostramos

# Ejecutamos el bucle principal de la ventana
ventana.mainloop()  # Iniciamos el bucle principal de eventos de tkinter
