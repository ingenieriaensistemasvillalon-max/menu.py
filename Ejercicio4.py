# Crear lista vacía
nombres = []

# Capturar 5 nombres
for i in range(5):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    nombres.append(nombre)  # Agregamos el nombre a la lista

# Mostrar lista original
print("\nLista original:", nombres)

# Mostrar primer elemento
print("Primer elemento:", nombres[0])

# Mostrar último elemento
print("Último elemento:", nombres[-1])

# Mostrar lista ordenada
print("Lista ordenada:", sorted(nombres))
