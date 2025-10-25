def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

try:
    segundos_str = input("Introducir la cantidad de segundos a convertir: ")
    
    segundos = int(segundos_str)
    
    if segundos < 0:
        print("La cantidad de segundos no puede ser negativa")
    else:
        horas_resultado = segundos_a_horas(segundos)
        
        print(f"\n--- Resultado de la Conversión ---")
        print(f"{segundos} segundos equivalen a {horas_resultado:.4f} horas")
        
except ValueError:
    print("La entrada debe ser un número entero válido")