from producto import Producto
import os

class Inventario:
    def _init_(self, archivo="inventario.txt"):
        self.lista_productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo."""
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w') as f:
                pass  # Crear archivo vacío si no existe
        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    if linea.strip():
                        producto = Producto.from_linea(linea)
                        self.lista_productos.append(producto)
            print("Inventario cargado correctamente.")
        except (FileNotFoundError, PermissionError, IOError) as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.lista_productos:
                    f.write(producto.to_linea())
            print("Inventario guardado correctamente.")
        except (PermissionError, IOError) as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar(self, producto):
        if any(p.obtener_id() == producto.obtener_id() for p in self.lista_productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.lista_productos.append(producto)
            self.guardar_inventario()
            print("Producto agregado correctamente.")

    def eliminar(self, id_producto):
        for p in self.lista_productos:
            if p.obtener_id() == id_producto:
                self.lista_productos.remove(p)
                self.guardar_inventario()
                print("Producto eliminado correctamente.")
                return
        print("No se encontró ningún producto con ese ID.")

    def actualizar(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.lista_productos:
            if p.obtener_id() == id_producto:
                if nueva_cantidad is not None:
                    p.cambiar_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.cambiar_precio(nuevo_precio)
                self.guardar_inventario()
                print("Producto actualizado correctamente.")
                return
        print("No se encontró ningún producto con ese ID.")

    def buscar(self, texto):
        resultados = [p for p in self.lista_productos if texto.lower() in p.obtener_nombre().lower()]
        if resultados:
            print("Resultados de la búsqueda:")
            for p in resultados:
                print(" ", p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual de la tienda de ropa y maquillaje:")
            for p in self.lista_productos:
                print(" ", p)