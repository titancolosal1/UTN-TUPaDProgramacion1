def potencia(base, exponente):
    if exponente == 0:
        return 1        
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")
