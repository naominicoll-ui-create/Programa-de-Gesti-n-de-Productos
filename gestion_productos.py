from abc import ABC, abstractmethod

class GestionProductos(ABC):
    @abstractmethod
    def mostrar_productos(self):
        pass

    @abstractmethod
    def introducir_producto(self, codigo, nombre, precio, cantidad):
        pass

    @abstractmethod
    def eliminar_producto(self, codigo):
        pass

    @abstractmethod
    def consultar_producto(self, codigo):
        pass

    @abstractmethod
    def modificar_precio(self, codigo, nuevo_precio):
        pass

    @abstractmethod
    def modificar_cantidad(self, codigo, nueva_cantidad):
        pass

    @abstractmethod
    def mostrar_productos_agotados(self):
        pass

    @abstractmethod
    def mostrar_productos_en_oferta(self, precio_max):
        pass
