from core.gestor import *


def menu():

    while True:

        print("\n==========================")
        print(" SISTEMA BIBLIOTECARIO ")
        print("==========================")

        print("1. Registrar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Eliminar libro")
        print("6. Mostrar libros")
        print("7. Estadisticas")
        print("8. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            try:
                codigo = int(input("Codigo: "))
                titulo = input("Titulo: ")
                autor = input("Autor: ")

                exito, mensaje = registrar_libro(
                    codigo,
                    titulo,
                    autor
                )

                print(mensaje)

            except ValueError:
                print("Debe ingresar un numero.")

        elif opcion == "2":

            try:
                codigo = int(input("Codigo: "))

                libro = buscar_libro(codigo)

                if libro:
                    print(libro)
                else:
                    print("Libro no encontrado.")

            except ValueError:
                print("Debe ingresar un numero.")

        elif opcion == "3":

            try:
                codigo = int(input("Codigo: "))
                exito, mensaje = prestar_libro(codigo)
                print(mensaje)

            except ValueError:
                print("Debe ingresar un numero.")

        elif opcion == "4":

            try:
                codigo = int(input("Codigo: "))
                exito, mensaje = devolver_libro(codigo)
                print(mensaje)

            except ValueError:
                print("Debe ingresar un numero.")

        elif opcion == "5":

            try:
                codigo = int(input("Codigo: "))

                if eliminar_libro(codigo):
                    print("Libro eliminado.")
                else:
                    print("Libro no encontrado.")

            except ValueError:
                print("Debe ingresar un numero.")

        elif opcion == "6":

            libros = listar_libros()

            if not libros:
                print("No hay libros registrados.")

            for libro in libros:
                print(libro)

        elif opcion == "7":

            estadisticas = obtener_estadisticas()

            print("\nESTADISTICAS")
            print("Total:", estadisticas["total"])
            print("Disponibles:", estadisticas["disponibles"])
            print("Prestados:", estadisticas["prestados"])

        elif opcion == "8":

            print("Gracias por usar el sistema.")
            break

        else:
            print("Opcion invalida.")