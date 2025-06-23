class Estudiante:
    def _init_(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre} - Nivel: {self.nivel}")

class ClaseDeBaile:
    def _init_(self, nombre_clase, estilo):
        self.nombre_clase = nombre_clase
        self.estilo = estilo
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante.nombre} fue inscrito(a) en la clase de {self.nombre_clase} ({self.estilo}).")

    def mostrar_estudiantes(self):
        print(f"Estudiantes en la clase {self.nombre_clase} ({self.estilo}):")
        if not self.estudiantes:
            print("  No hay estudiantes inscritos aún.")
        else:
            for e in self.estudiantes:
                print(f"  - {e.nombre} (Nivel: {e.nivel})")

class EstudioDeBaile:
    def _init_(self, nombre_estudio):
        self.nombre_estudio = nombre_estudio
        self.clases = []

    def agregar_clase(self, clase):
        self.clases.append(clase)
        print(f"Clase {clase.nombre_clase} ({clase.estilo}) agregada al estudio {self.nombre_estudio}.")

    def mostrar_clases(self):
        print(f"Clases disponibles en {self.nombre_estudio}:")
        for clase in self.clases:
            print(f"- {clase.nombre_clase} ({clase.estilo})")

    def mostrar_todo(self):
        print(f"\n--- Estado completo del estudio de baile '{self.nombre_estudio}' ---")
        for clase in self.clases:
            clase.mostrar_estudiantes()
        print("---------------------------------------------------------------\n")

if __name__ == "_main_":
    estudio = EstudioDeBaile("Estudio Kimverly Dance")
    clase1 = ClaseDeBaile("Clases de K-Pop", "K-Pop")
    clase2 = ClaseDeBaile("Taller de Hip-Hop", "Hip-Hop")
    clase3 = ClaseDeBaile("Danza Contemporánea", "Contemporáneo")

    estudio.agregar_clase(clase1)
    estudio.agregar_clase(clase2)
    estudio.agregar_clase(clase3)

    estudiante1 = Estudiante("Kimverly", "Intermedio")
    estudiante2 = Estudiante("Alex", "Principiante")
    estudiante3 = Estudiante("Sofia", "Avanzado")

    clase1.inscribir_estudiante(estudiante1)
    clase2.inscribir_estudiante(estudiante2)
    clase3.inscribir_estudiante(estudiante3)
    clase1.inscribir_estudiante(estudiante3)

    estudio.mostrar_clases()
    estudio.mostrar_todo()



