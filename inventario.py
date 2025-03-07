from gestion_productos import GestionProductos
from producto import Producto

class Inventario(GestionProductos):
    def __init__(self):
        self.productos = {
            "001": Producto("001", "Laptop", 800.0, 10),
            "002": Producto("002", "Mouse", 20.0, 0),
            "003": Producto("003", "Teclado", 50.0, 5),
            "004": Producto("004", "Monitor", 200.0, 0),
            "005": Producto("005", "Auriculares", 15.0, 20),
            "006": Producto("006", "Impresora", 150.0, 3),
            "007": Producto("007", "Cámara Web", 30.0, 8),
            "008": Producto("008", "Disco Duro Externo", 100.0, 15),
            "009": Producto("009", "Pantalla Táctil", 120.0, 7),
            "010": Producto("010", "Micrófono", 40.0, 12)
        }

    def mostrar_productos(self):
        return [str(producto) for producto in self.productos.values()]

    def introducir_producto(self, codigo, nombre, precio, cantidad):
        if codigo in self.productos:
            return "Error: Código ya existente"
        self.productos[codigo] = Producto(codigo, nombre, precio, cantidad)
        return "Producto agregado correctamente"

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            return "Producto eliminado correctamente"
        return "Error: Producto no encontrado"

    def consultar_producto(self, codigo):
        return str(self.productos.get(codigo, "Error: Producto no encontrado"))

    def modificar_precio(self, codigo, nuevo_precio):
        if codigo in self.productos:
            self.productos[codigo].precio = nuevo_precio
            return "Precio actualizado correctamente"
        return "Error: Producto no encontrado"

    def modificar_cantidad(self, codigo, nueva_cantidad):
        if codigo in self.productos:
            self.productos[codigo].cantidad = nueva_cantidad
            return "Cantidad actualizada correctamente"
        return "Error: Producto no encontrado"

    def mostrar_productos_agotados(self):
        return [str(producto) for producto in self.productos.values() if producto.cantidad == 0]

    def mostrar_productos_en_oferta(self, precio_max):
        return [str(producto) for producto in self.productos.values() if producto.precio < precio_max]
