import math

def calcular_area_circulo(radio):

    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):

    perimetro = 2 * math.pi * radio
    return perimetro

try:
    radio_str = input("Introducir el radio del círculo: ")
    radio = float(radio_str)
    
    if radio < 0:
        print("El radio no puede ser negativo.")
    else:
        area_resultado = calcular_area_circulo(radio)
        
        perimetro_resultado = calcular_perimetro_circulo(radio)
        
        print(f"\n--- Resultados para el radio {radio} ---")
        print(f"El area del círculo es: {area_resultado:.4f}")
        print(f"El perímetro del círculo es: {perimetro_resultado:.4f}")

except ValueError:
    print("La entrada no es válida")