def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Datos del usuario")
        print("2 Evaluar numero")
        print("3 Suma y promedio")
        print("4 Lista de estudiantes")
        print("5 Área de rectángulo ")
        print("6 Información del alumno ")
        print("7  Mostrar todos los datos")
      print("0. Salir")
        
      opcion = input("Elige una opción: ")

        if opcion == "1":
            ejercicio1()
        elif opcion == "0":
          
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
