# Menú interactivo hecho como estudiante :)

# Función 1: Datos del usuario
def datos_usuario():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print("Nombre:", nombre)
    print("Edad:", edad)

# Función 2: Evaluar número
def evaluar_numero():
    n = float(input("Ingresa un número: "))
    if n > 0:
        print("El número es positivo")
    elif n < 0:
        print("El número es negativo")
    else:
        print("El número es cero")

# Función 3: Suma y promedio
def suma_promedio():
    n = int(input("¿Cuántos números vas a capturar? "))
    suma = 0
    for i in range(n):
        num = float(input(f"Número {i+1}: "))
        suma += num
    promedio = suma / n
    print("Cantidad ingresada:", n)
    print("Suma total:", suma)
    print("Promedio:", promedio)

# Función 4: Lista de estudiantes
def lista_estudiantes():
    lista = []
    for i in range(5):
        nombre = input(f"Ingrese el estudiante {i+1}: ")
        lista.append(nombre)

    print("Lista original:", lista)
    print("Primer elemento:", lista[0])
    print("Último elemento:", lista[-1])
    print("Lista ordenada:", sorted(lista))

# Función 5: Área de rectángulo
def area_rectangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = base * altura
    print("El área es:", area)

# Función 6: Información del alumno
def info_alumno():
    nombre = input("Nombre del alumno: ")
    grupo = input("Grupo: ")
    materia = input("Materia: ")

    print("Alumno:", nombre)
    print("Grupo:", grupo)
    print("Materia:", materia)

# Función 7: No guarda nada, solo dice que no hay datos
def mostrar_todos():
    print("Este menú es sencillo, no se guardan datos :)")
    print("Cada opción solo muestra resultados al momento.")


# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n MENÚ PRINCIPAL ")
        print("1. Datos del usuario")
        print("2. Evaluar número")
        print("3. Suma y promedio")
        print("4. Lista de estudiantes")
        print("5. Área del rectángulo")
        print("6. Información del alumno")
        print("7. Mostrar todos los datos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            datos_usuario()
        elif opcion == "2":
            evaluar_numero()
        elif opcion == "3":
            suma_promedio()
        elif opcion == "4":
            lista_estudiantes()
        elif opcion == "5":
            area_rectangulo()
        elif opcion == "6":
            info_alumno()
        elif opcion == "7":
            mostrar_todos()
        elif opcion == "0":
            print("Adiós!")
            break
        else:
            print("Opción no válida.")

# Ejecutar menú
menu()
