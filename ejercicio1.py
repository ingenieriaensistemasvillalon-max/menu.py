# practica1.py

# 1. Captura de datos con input()
nombre = input("Como te llamas?: ")
print ("Hola",nombre)
edad= int(input("¿Cuantos años tienes?"))
print("tendras" edad +1, "años el proximo año")

try:
numero= int(input("Escribe un numero:"))
print("El numero es", numero)
except ValvueError:
print("Eso no es un numero valido")
