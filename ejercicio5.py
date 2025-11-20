# Definición de la función
def area_rectangulo(base, altura):
    area = base * altura  # Calculamos el área
    return area           # Retornamos el resultado

# Pedimos los valores al usuario
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Llamamos a la función y guardamos el resultado
resultado = area_rectangulo(base, altura)

# Imprimimos el área
print("El área del rectángulo es:", resultado)
