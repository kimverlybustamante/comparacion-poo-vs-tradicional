# Clase Mascota que demuestra el uso de constructor y destructor
class Mascota:
    def _init_(self, nombre, tipo):
        """
        Constructor: se ejecuta al crear un objeto de tipo Mascota.
        Inicializa el nombre y el tipo de la mascota (perro, gato.)
        """
        self.nombre = nombre
        self.tipo = tipo
        print(f"{self.tipo} llamado {self.nombre} ha sido adoptado.")

    def presentarse(self):
        """Método para que la mascota se presente"""
        print(f"Hola, soy un {self.tipo} y me llamo {self.nombre}.")

    def _del_(self):
        """
        Destructor: se ejecuta cuando el objeto es eliminado o es cerrado.
        Aquí  va a simular que la mascota se va o se elimina.
        """
        print(f"{self.tipo} llamado {self.nombre} ha salido del programa.")


# Crear un objeto de la clase Mascota
mi_mascota = Mascota("Lia", "gato")
mi_mascota.presentarse()

# Eliminar el objeto (esto activará el destructor)
del mi_mascota