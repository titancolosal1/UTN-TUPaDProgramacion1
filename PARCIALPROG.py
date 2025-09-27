# 1 INICIALIZACIÓN DE LISTAS, VARIABLES, ETC.
titulos = []
ejemplares = []
opcion = 0
SALIR = 8



while opcion != SALIR:
# 2 MENÚ
    print("\n" + "="*50)
    print("        GESTIÓN DE CATÁLOGO BIBLIOTECARIO")
    print("="*50)
    print("1. Ingresar títulos iniciales (Modo Lote)")
    print("2. Ingresar ejemplares (Añadir Stock a existentes)")
    print("3. Mostrar catálogo completo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados (Stock 0)")
    print("6. Agregar título (Individual)")
    print("7. Actualizar ejemplares (Préstamo/Devolución)")
    print(f"8. Salir")
    print("-" * 50)

# 3 MANEJO DE LA OPCIÓN ESTRUCTURA DE CONTROL (IF/ELIF/ELSE)
    
    # Valida que la opción exista
    entrada_opcion = input("Seleccione una opción (1-8): ")
    if entrada_opcion.isdigit():
        opcion = int(entrada_opcion)
    else:
        opcion = 0 
        print("Entrada no válida. Por favor, ingrese un número.")
        continue #Vuelve al inicio del while

    #Opción 1: Ingresar titulos por lote
    if opcion == 1:
        print("\n--- INGRESAR TÍTULOS INICIALES (LOTE) ---")
        num_titulos_str = input("¿Cuántos títulos diferentes desea ingresar en este lote?: ")
        
        if num_titulos_str.isdigit() and int(num_titulos_str) > 0:
            num_titulos = int(num_titulos_str)
            
            for i in range(num_titulos):
                print(f"\n--- Título {i + 1} de {num_titulos} ---")
                nuevo_titulo = input("Ingrese el título del libro: ").strip()
                cant_str = input(f"Ingrese la cantidad de ejemplares iniciales para '{nuevo_titulo}': ")

                # Validar título y cantidad
                if not nuevo_titulo:
                    print("El título no puede estar vacío. Saltando al siguiente.")
                    continue
                elif nuevo_titulo.lower() in [t.lower() for t in titulos]:
                    print(f"El título '{nuevo_titulo}' ya existe. Use Opción 2 para añadir stock. Saltando al siguiente.")
                    continue
                elif not cant_str.isdigit() or int(cant_str) < 0:
                    print("Cantidad inicial inválida. Debe ser un número entero no negativo. Saltando al siguiente.")
                    continue
                
                # Insertar en listas
                titulos.append(nuevo_titulo)
                ejemplares.append(int(cant_str)) 
                print(f"Título '{nuevo_titulo}' agregado con {int(cant_str)} ejemplares.")
        else:
            print("Cantidad de títulos a ingresar no válida.")

    #Opción 2: Ingresar Ejemplares
    elif opcion == 2:
        print("\n--- AÑADIR STOCK A EJEMPLARES EXISTENTES ---")
        titulo_buscado = input("Ingrese el título al que desea añadir stock: ").strip()

        if titulo_buscado in titulos:
            indice = titulos.index(titulo_buscado)
            
            cant_str = input(f"Ingrese la cantidad de ejemplares a añadir a '{titulo_buscado}': ")
            if cant_str.isdigit() and int(cant_str) > 0:
                cantidad = int(cant_str)
                ejemplares[indice] += cantidad 
                print(f"Stock actualizado. Nuevo total: {ejemplares[indice]} ejemplares.")
            else:
                print("Cantidad inválida. Debe ser un número entero positivo.")

        else:
            print(f"El título '{titulo_buscado}' no se encuentra en el catálogo.")

    #Opción 3: Mostrar Catálogo
    elif opcion == 3:
        print("\n--- CATÁLOGO COMPLETO ---")
        if not titulos:
            print("El catálogo está vacío.")
        else:
            print(f"Total de libros únicos: {len(titulos)}")
            print("-" * 50)
            for i in range(len(titulos)):
                # El 'i' vincula el título con su stock
                print(f"Título: {titulos[i]:<40} | Stock: {ejemplares[i]}")
            print("-" * 50)

    #Opción 4: Consultar Disponibilidad
    elif opcion == 4:
        print("\n--- CONSULTAR DISPONIBILIDAD ---")
        titulo_buscado = input("Ingrese el título a consultar: ").strip()
        
        if titulo_buscado in titulos:
            indice = titulos.index(titulo_buscado)
            stock = ejemplares[indice]
            print(f"El libro '{titulo_buscado}' tiene {stock} ejemplares disponibles.")
        else:
            print(f"El título '{titulo_buscado}' no se encuentra en el catálogo.")

    #Opción 5: Títulos Agotados
    elif opcion == 5:
        print("\n--- TÍTULOS AGOTADOS (STOCK 0) ---")
        agotados_encontrados = False
        
        for i in range(len(ejemplares)):
            if ejemplares[i] == 0:
                print(f"AGOTADO: {titulos[i]}")
                agotados_encontrados = True
                
        if not agotados_encontrados:
            print("No hay títulos agotados/todo tiene stock.")

    #Lógica de la Opción 6: Agregar Título (Individual)
    elif opcion == 6:
        print("\nAGREGAR NUEVO TÍTULO Y STOCK INDIVIDUALMENTE")
        nuevo_titulo = input("Ingrese el título del nuevo libro: ").strip()
        cant_str = input(f"Ingrese la cantidad de ejemplares iniciales para '{nuevo_titulo}': ")

        # Validación
        if not nuevo_titulo:
            print("El título no puede estar vacío.")
        elif nuevo_titulo.lower() in [t.lower() for t in titulos]:
            print(f"El título '{nuevo_titulo}' ya existe. Use Opción 2 para añadir stock.")
        elif not cant_str.isdigit() or int(cant_str) < 0:
            print("Cantidad inicial inválida. Debe ser un número entero no negativo.")
        else:
            # Inserción en listas paralelas
            titulos.append(nuevo_titulo)
            ejemplares.append(int(cant_str)) 
            print(f"Título '{nuevo_titulo}' agregado con {int(cant_str)} ejemplares.")

    #Opción 7: Actualizar ejemplares (Préstamo/Devolución)
    elif opcion == 7:
        print("\nACTUALIZAR EJEMPLARES (PRÉSTAMO/DEVOLUCIÓN)")
        titulo_buscado = input("Ingrese el título a modificar: ").strip()

        if titulo_buscado in titulos:
            indice = titulos.index(titulo_buscado)
            
            print(f"\nStock actual de '{titulo_buscado}': {ejemplares[indice]}")
            print("A. Préstamo (-1 ejemplar)")
            print("B. Devolución (+1 ejemplar)")
            accion = input("Seleccione A o B: ").upper()
            
            if accion == 'A': # Préstamo
                if ejemplares[indice] > 0:
                    ejemplares[indice] -= 1 # Reduce el stock
                    print(f"Préstamo registrado. Nuevo stock: {ejemplares[indice]}")
                else:
                    print("Stock agotado (0 ejemplares). No se puede realizar el préstamo")
            elif accion == 'B': # Devolucion
                ejemplares[indice] += 1 # Incrementa el stock
                print(f"Devolución registrada. Nuevo stock: {ejemplares[indice]}")
            else:
                print("Opción de acción inválida. No se realizó ningún cambio")

        else:
            print(f"El título '{titulo_buscado}' no se encuentra en el catálogo")


    #Opción 8: Salir
    elif opcion == SALIR:
        print("\nSaliendo del sistema")
    else:
        print("Opción no reconocida. Por favor, ingrese un número del 1 al 8")

#Fin