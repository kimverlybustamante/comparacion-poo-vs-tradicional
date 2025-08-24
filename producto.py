class Producto:
    def _init_(self, id_producto, nombre, categoria, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria   # "ropa" o "maquillaje"
        self.cantidad = cantidad
        self.precio = precio

    # Métodos "get"
    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_categoria(self):
        return self.categoria

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos "set"
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def cambiar_categoria(self, nueva_categoria):
        self.categoria = nueva_categoria

    def cambiar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Representación del producto
    def _str_(self):
        return f"[{self.id}] {self.nombre} ({self.categoria}) - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    # Método para guardar en archivo
    def to_linea(self):
        """Devuelve una línea que puede escribirse en el archivo"""
        return f"{self.id},{self.nombre},{self.categoria},{self.cantidad},{self.precio}\n"

    # Método para crear un producto desde una línea de archivo
    @classmethod
    def from_linea(cls, linea):
        id_producto, nombre, categoria, cantidad, precio = linea.strip().split(',')
        return cls(int(id_producto), nombre, categoria, int(cantidad), float(precio))