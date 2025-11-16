from funciones import *

ARCHIVO = "paises.csv"

def menu():
    paises = cargar_paises(ARCHIVO)

    while True:
        print("\n=== MENÚ ===")
        print("1. Agregar país")
        print("2. Actualizar datos de un país")
        print("3. Buscar país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)
            guardar_paises(ARCHIVO, paises)
        elif opcion == "2":
            actualizar_pais(paises)
            guardar_paises(ARCHIVO, paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
