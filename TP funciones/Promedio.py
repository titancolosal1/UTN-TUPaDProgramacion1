def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

try:
    num1_str = input("Introducir el primer número: ")
    num2_str = input("Introducir el segundo número: ")
    num3_str = input("Introducir el tercer número: ")
    
    num1 = float(num1_str)
    num2 = float(num2_str)
    num3 = float(num3_str)
    
    promedio_resultado = calcular_promedio(num1, num2, num3)
    
    print(f"\n--- Resultado ---")
    print(f"Los números ingresados son: {num1}, {num2}, {num3}")
    print(f"El promedio de los tres números es: {promedio_resultado:.2f}")

except ValueError:
    print("Asegurate de introducir números válidos")