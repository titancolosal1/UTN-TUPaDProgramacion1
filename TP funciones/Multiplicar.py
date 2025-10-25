def tabla_multiplicar(numero):
    print(f"\n--- Tabla de Multiplicar del {numero} ---")
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero_str = input("Por favor, introduce el número para generar su tabla de multiplicar: ")
    
    numero = int(numero_str)
    
    tabla_multiplicar(numero)
    
except ValueError:
    print("Error: La entrada debe ser un número entero válido.")