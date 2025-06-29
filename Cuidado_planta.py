# Este programa ayuda a cuidar una planta.
# Verificae si recibió suficiente agua hoy según su rutina.

# Solicita el nombre de la planta (tipo de dato: string)
nombre_planta = input("¿Cómo se llama tu planta? ")

# Solicita la cantidad de agua que recibió hoy (tipo de dato: float)
agua_recibida = float(input("¿Cuánta agua recibió hoy en mililitros? "))

# Solicita cada cuántos días se debe regar (tipo de dato: integer)
frecuencia_riego = int(input("¿Cada cuántos días debes regarla? "))

# Determina si recibió suficiente agua (tipo de dato: boolean)
riego_suficiente = agua_recibida >= 90

# Muestra el resumen de cuidado
print("\nReporte de cuidado para", nombre_planta)
print("Agua recibida hoy:", agua_recibida, "ml")
print("Frecuencia recomendada de riego:", frecuencia_riego, "días")
print("¿Recibió suficiente agua hoy?", riego_suficiente)

# Mensaje final según el riego
if riego_suficiente:
    print(nombre_planta, "está bien hidratada. Bien hecho.")
else:
    print("A", nombre_planta, "le falta un poco más de agua. No olvides regarla.")