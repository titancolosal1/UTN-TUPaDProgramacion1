def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "Indefinida"
        
    return (suma, resta, multiplicacion, division)

try:
    num1_str = input("Introducir el primer número")
    num2_str = input("Introducir el segundo número")
    
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    resultados_tupla = operaciones_basicas(num1, num2)
    
    suma_res, resta_res, mult_res, div_res = resultados_tupla
    
    print(f"\n--- Operaciones con a={num1} y b={num2} ---")
    print(f"Suma (a + b):         {suma_res}")
    print(f"Resta (a - b):        {resta_res}")
    print(f"Multiplicación (a * b): {mult_res}")
    print(f"División (a / b):     {div_res}")

except ValueError:
    print("Ambas entradas deben ser números válidos")