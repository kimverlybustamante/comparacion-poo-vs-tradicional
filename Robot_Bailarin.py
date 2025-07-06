# --------------------------------------
# Programa: Sistema de Robots Bailarines
# Conceptos de Programación Orientada a Objetos (POO) aplicados:
# - Clase: definición de plantillas de robots
# - Objeto: instancias como kini_bot y hiphop_bot
# - Herencia: KiniBot y RobotHipHop heredan de RobotBailarín
# - Encapsulación: atributos privados como __velocidad y __energia
# - Polimorfismo: el método bailar() se comporta diferente según el robot
# --------------------------------------

# Clase base: RobotBailarín
class RobotBailarín:
    def _init_(self, nombre, estilo_base):
        self._nombre = nombre  # Atributo protegido
        self._estilo_base = estilo_base

    def bailar(self):  # Método base que será sobrescrito (polimorfismo)
        return f"{self._nombre} realiza un baile básico de {self._estilo_base}"

    def info(self):
        return f"Robot: {self._nombre} | Estilo base: {self._estilo_base}"


# Clase derivada: KiniBot (robot personalizado con tu nombre)
class KiniBot(RobotBailarín):
    def _init_(self, velocidad):
        super()._init_("KiniBot", "K-Pop")
        self.__velocidad = velocidad  # Atributo privado (encapsulación)

    def bailar(self):  # Polimorfismo
        return f"{self.nombre} presenta una coreografía de K-Pop con velocidad {self._velocidad}"

    def get_velocidad(self):
        return self.__velocidad


# Otra clase derivada: RobotHipHop
class RobotHipHop(RobotBailarín):
    def _init_(self, nombre, energia):
        super()._init_(nombre, "Hip-Hop")
        self.__energia = energia  # Atributo privado

    def bailar(self):  # Polimorfismo
        return f"{self.nombre} realiza movimientos de breakdance con energía {self._energia}"

    def get_energia(self):
        return self.__energia


# Crear instancias de los robots
kini_bot = KiniBot(velocidad=9)
hiphop_bot = RobotHipHop("BreakX", energia=10)

# Usar los métodos y mostrar resultados
print(kini_bot.info())
print(kini_bot.bailar())
print("Velocidad de baile:", kini_bot.get_velocidad())

print("\n" + hiphop_bot.info())
print(hiphop_bot.bailar())
print("Nivel de energía:", hiphop_bot.get_energia())