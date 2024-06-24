# Definición de la clase base Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def get_precio(self):
        return self.precio
    
    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

# Definición de la subclase ProductoFresco
class ProductoFresco(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_caducidad):
        super().__init__(nombre, precio, cantidad)
        self.fecha_caducidad = fecha_caducidad
    
    def verificar_caducidad(self):
        # Supongamos que la fecha actual es 2024-06-20 y caduca en 2024-06-30
        if self.fecha_caducidad < "2024-06-30":
            print(f"{self.nombre} está próximo a caducar. Verificar stock.")
        else:
            print(f"{self.nombre} tiene tiempo antes de caducar.")



# Función principal main
def main():
    # Creación de instancias de productos frescos y no frescos
    producto_fresco = ProductoFresco("Leche", 25.50, 10, "2024-06-30")
    
    # Mostrar información de los productos
    print("Informacion del Producto Fresco:")
    print(f"Nombre: {producto_fresco.nombre}")
    print(f"Precio: S/ {producto_fresco.get_precio()}")
    print(f"Cantidad en stock: {producto_fresco.get_cantidad()}")
    producto_fresco.verificar_caducidad()
    print()
    
   
# Llamada a la función principal main
if __name__ == "__main__":
    main()
