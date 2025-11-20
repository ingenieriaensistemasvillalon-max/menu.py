import random

# Función para clasificar números en pares e impares
def clasificar_numeros(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Generar lista de 10 números aleatorios entre 1 y 50
numeros = [random.randint(1, 50) for _ in range(10)]
print("Números generados:", numeros)

# Clasificar los números
pares, impares = clasificar_numeros(numeros)
print("Números pares:", pares)
print("Números impares:", impares)
