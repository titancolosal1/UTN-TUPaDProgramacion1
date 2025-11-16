# Archivo: gestion_productos.py

# 1. Crear archivo inicial (si no existe)
import os

if not os.path.exists("productos.txt"):
    with open("productos.txt", "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,250.0,50\n")
        f.write("Borrador,80.0,40\n")

# Función para leer productos desde el archivo y cargarlos en lista de diccionarios
def leer_productos():
    productos = []
    with open("productos.txt", "r") as f:
        for linea in f:
            linea = linea.strip()
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

# Función para mostrar productos
def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Función para agregar un producto desde teclado y al archivo
def agregar_producto():
    print("\nIngrese un nuevo producto:")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    with open("productos.txt", "a") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")
    print(f"Producto {nombre} agregado correctamente.")

# Función para buscar un producto por nombre
def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ")
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado: {p}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

# Función para guardar productos desde la lista al archivo (sobrescribir)
def guardar_productos(productos):
    with open("productos.txt", "w") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("\nArchivo actualizado correctamente.")

# Programa principal
productos = leer_productos()
mostrar_productos(productos)
agregar_producto()

# Leer nuevamente para incluir el producto agregado
productos = leer_productos()
buscar_producto(productos)

# Guardar productos actualizados (por si se hicieron cambios en memoria)
guardar_productos(productos)
