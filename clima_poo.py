class ClimaSemanal:
    def _init_(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingresa la temperatura de día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es de: {promedio:.2f}°C")


# Crear instancia y ejecutar
clima = ClimaSemanal()
clima.ingresar_temperaturas()
clima.mostrar_promedio()