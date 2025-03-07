import tkinter as tk
from tkinter import messagebox
from inventario import Inventario

class App:
    def __init__(self, root):
        self.inventario = Inventario()
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.configure(bg="#9F81F7")

        self.frame = tk.Frame(root, bg="#9F81F7")
        self.frame.pack(pady=20)

        self.lbl_codigo = tk.Label(self.frame, text="Código:", bg="#9F81F7")
        self.lbl_codigo.grid(row=0, column=0)
        self.entry_codigo = tk.Entry(self.frame)
        self.entry_codigo.grid(row=0, column=1)

        self.lbl_nombre = tk.Label(self.frame, text="Nombre:", bg="#9F81F7")
        self.lbl_nombre.grid(row=1, column=0)
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=1, column=1)

        self.lbl_precio = tk.Label(self.frame, text="Precio:", bg="#9F81F7")
        self.lbl_precio.grid(row=2, column=0)
        self.entry_precio = tk.Entry(self.frame)
        self.entry_precio.grid(row=2, column=1)

        self.lbl_cantidad = tk.Label(self.frame, text="Cantidad:", bg="#9F81F7")
        self.lbl_cantidad.grid(row=3, column=0)
        self.entry_cantidad = tk.Entry(self.frame)
        self.entry_cantidad.grid(row=3, column=1)

        self.btn_agregar = tk.Button(self.frame, text="Agregar Producto", command=self.agregar_producto)
        self.btn_agregar.grid(row=4, columnspan=2, pady=5)

        self.btn_eliminar = tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto)
        self.btn_eliminar.pack(pady=5)

        self.btn_modificar_cantidad = tk.Button(root, text="Modificar Cantidad", command=self.modificar_cantidad)
        self.btn_modificar_cantidad.pack(pady=5)

        self.btn_modificar_precio = tk.Button(root, text="Modificar Precio", command=self.modificar_precio)
        self.btn_modificar_precio.pack(pady=5)

        self.btn_mostrar = tk.Button(root, text="Mostrar Productos", command=self.mostrar_productos)
        self.btn_mostrar.pack(pady=5)

        self.btn_consultar = tk.Button(root, text="Consultar Producto", command=self.consultar_producto)
        self.btn_consultar.pack(pady=5)

        self.btn_mostrar_agotados = tk.Button(root, text="Mostrar Productos Agotados", command=self.mostrar_productos_agotados)
        self.btn_mostrar_agotados.pack(pady=5)

        self.btn_mostrar_oferta = tk.Button(root, text="Mostrar Productos en Oferta", command=self.mostrar_productos_oferta)
        self.btn_mostrar_oferta.pack(pady=5)

        self.txt_resultado = tk.Text(root, height=10, width=50)
        self.txt_resultado.pack()

    def agregar_producto(self):
        # Obtener los valores de las entradas
        codigo = self.entry_codigo.get()
        nombre = self.entry_nombre.get()
        try:
            precio = float(self.entry_precio.get())
            cantidad = int(self.entry_cantidad.get())
            # Llamar a la función de agregar producto en el inventario
            mensaje = self.inventario.introducir_producto(codigo, nombre, precio, cantidad)
        except ValueError:
            mensaje = "Error: Precio y cantidad deben ser números"
        messagebox.showinfo("Resultado", mensaje)

    def eliminar_producto(self):
        # Obtener el código del producto a eliminar
        codigo = self.entry_codigo.get()
        # Llamar a la función de eliminar producto en el inventario
        mensaje = self.inventario.eliminar_producto(codigo)
        messagebox.showinfo("Resultado", mensaje)

    def modificar_cantidad(self):
        # Obtener el código y cantidad para modificar
        codigo = self.entry_codigo.get()
        try:
            cantidad = int(self.entry_cantidad.get())
            # Llamar a la función para modificar la cantidad del producto
            mensaje = self.inventario.modificar_cantidad(codigo, cantidad)
        except ValueError:
            mensaje = "Error: La cantidad debe ser un número"
        messagebox.showinfo("Resultado", mensaje)

    def modificar_precio(self):
        # Obtener el código y precio para modificar
        codigo = self.entry_codigo.get()
        try:
            precio = float(self.entry_precio.get())
            # Llamar a la función para modificar el precio del producto
            mensaje = self.inventario.modificar_precio(codigo, precio)
        except ValueError:
            mensaje = "Error: El precio debe ser un número"
        messagebox.showinfo("Resultado", mensaje)

    def mostrar_productos(self):
        # Mostrar todos los productos
        productos = self.inventario.mostrar_productos()
        self.txt_resultado.delete(1.0, tk.END)
        for producto in productos:
            self.txt_resultado.insert(tk.END, producto + "\n")

    def consultar_producto(self):
        # Consultar un producto específico por código
        codigo = self.entry_codigo.get()
        mensaje = self.inventario.consultar_producto(codigo)
        messagebox.showinfo("Resultado", mensaje)

    def mostrar_productos_agotados(self):
        # Mostrar productos que están agotados (cantidad 0)
        productos = self.inventario.mostrar_productos_agotados()
        self.txt_resultado.delete(1.0, tk.END)
        for producto in productos:
            self.txt_resultado.insert(tk.END, producto + "\n")

    def mostrar_productos_oferta(self):
        # Mostrar productos con precio bajo
        try:
            precio_max = float(self.entry_precio.get())
            productos = self.inventario.mostrar_productos_en_oferta(precio_max)
            self.txt_resultado.delete(1.0, tk.END)
            for producto in productos:
                self.txt_resultado.insert(tk.END, producto + "\n")
        except ValueError:
            messagebox.showinfo("Error", "El precio debe ser un número")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
