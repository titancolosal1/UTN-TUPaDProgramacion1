ventas = [
    [10, 12, 15, 20, 18, 22, 25],  #Producto1
    [5, 7, 9, 10, 6, 8, 12],       #Producto2
    [14, 11, 13, 17, 15, 19, 20],  #Producto3
    [9, 8, 7, 6, 12, 10, 15]       #Producto4
]

print("Total vendido por cada producto:")
for i, fila in enumerate(ventas):
    total = sum(fila)
    print(f"Producto {i+1}: {total}")

totales_dias = [sum(ventas[fila][dia] for fila in range(4)) for dia in range(7)]
dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"\nDía con mayores ventas totales: Día {dia_max} (ventas = {max(totales_dias)})")

totales_productos = [sum(fila) for fila in ventas]
producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"\nProducto más vendido en la semana: Producto {producto_max} (ventas = {max(totales_productos)})")
