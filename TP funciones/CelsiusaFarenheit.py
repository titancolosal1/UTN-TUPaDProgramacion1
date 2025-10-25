def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

try:
    celsius_str = input("Introducir la temperatura en Celsius (°C): ")
    
    celsius = float(celsius_str)

    fahrenheit_resultado = celsius_a_fahrenheit(celsius)
    
    print(f"\n--- Resultado ---")
    print(f"La temperatura de {celsius:.2f}°C equivale a {fahrenheit_resultado:.2f}°F")

except ValueError:
    print("La entrada debe ser un número válido")