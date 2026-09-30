# Pedimos el nombre al usuario
nombre = input("¿Cómo te llamas?: ")

# Pedimos el año de nacimiento y lo convertimos a un número entero (int)
anio_nacimiento = int(input("¿En qué año naciste?: "))

# Calculamos la edad restando el año de nacimiento al año actual (2026)
anio_actual = 2026
edad = anio_actual - anio_nacimiento

# Mostramos el resultado en la pantalla
print(f"¡Un placer conocerte, {nombre}! Este año cumplirás {edad} años.")
