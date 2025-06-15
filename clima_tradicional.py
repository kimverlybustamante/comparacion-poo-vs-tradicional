# Función ingresar las temperaturas
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingresa la temperatura de día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función calcular promedio
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es de: {promedio:.2f}°C")

# Ejecutar el programa
main()