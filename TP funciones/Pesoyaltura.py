def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

try:
    peso_str = input("Introduce tu peso en kilos (kg): ")
    altura_str = input("Introduce tu altura en metros (m): ")
    
    peso = float(peso_str)
    altura = float(altura_str)
    
    if peso <= 0 or altura <= 0:
        print("El peso y la altura deben ser valores positivos")
    else:
        imc_resultado = calcular_imc(peso, altura)
        print(f"\n--- Resultado del Cálculo del IMC ---")
        print(f"Peso: {peso} kg, Altura: {altura} m")
        print(f"Tu indice de masa corporal (IMC) es: **{imc_resultado:.2f}**")

except ValueError:
    print("Introducir solo números válidos para el peso y la altura")