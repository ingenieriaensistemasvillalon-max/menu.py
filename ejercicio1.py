# practica1.py

# 1. Captura de datos con input()
nombre = input("Ingresa tu nombre: ")
edad = int(input("¿Cuantos años tienes?"))
estudias = input("¿Que carrera estudias?"))

# 2. Conversión de tipos
nombre = int(nombre)
edad = int(edad)
estudias = int(estudias)

# 3. Mostrar los datos capturados
print("\n--- Datos Capturados ---")
print("Nombre completo:", nombre)
print("Edad:", edad)
print("¿Que carrera estudia?:", estudias)

# 4. Mostrar el tipo de cada variable
print("\n--- Tipos de Datos ---")
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("¿Que carrera estudia?:", estudias)
