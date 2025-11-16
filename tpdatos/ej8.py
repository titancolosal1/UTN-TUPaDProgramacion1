productos = {
    "Leche": 10,
    "Pan": 20,
    "Huevos": 30
}

while True:
    print("\nOpciones:")
    print("1 - Consultar stock")
    print("2 - Agregar unidades a un producto existente")
    print("3 - Agregar un nuevo producto")
    print("4 - Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto a consultar: ")
        if nombre in productos:
            print(f"El stock de {nombre} es: {productos[nombre]}")
        else:
            print(f"{nombre} no existe en el inventario.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        if nombre in productos:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            productos[nombre] += cantidad
            print(f"Nuevo stock de {nombre}: {productos[nombre]}")
        else:
            print(f"{nombre} no existe en el inventario.")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del nuevo producto: ")
        if nombre in productos:
            print(f"{nombre} ya existe. Use la opción 2 para agregar unidades.")
        else:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            productos[nombre] = cantidad
            print(f"{nombre} agregado con stock {cantidad}.")
    
    elif opcion == "4":
        print("Saliendo")
        break
    
    else:
        print("Opción no válida, intente de nuevo.")
