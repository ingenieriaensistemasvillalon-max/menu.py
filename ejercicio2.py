# Pedir al usuario la cantidad de números
n = int(input("¿Cuántos números vas a ingresar? "))

# Inicializar acumulador para la suma
suma_total = 0

# Ciclo para capturar n números
for i in range(n):
    numero = float(input(f"Ingresa el número {i+1}: "))
    suma_total += numero  # Acumulamos la suma

# Calcular promedio
promedio = suma_total / n

# Mostrar resultados
print("\nCantidad ingresada:", n)
print("Suma total:", suma_total)
print("Promedio:", promedio)
