def puerta_and(a, b):
    # La operación AND es equivalente a la multiplicación en lógica binaria
    return a * b

def puerta_or(a, b):
    # La operación OR es 1 si a es 1 o b es 1.
    if a == 1 or b == 1:
        return 1
    else:
        return 0

def puerta_not(a):
    # La operación NOT invierte el valor
    if a == 1:
        return 0
    else:
        return 1
    
def puerta_nand(a, b):
    # La operación AND es equivalente a la multiplicación en lógica binaria
    if (a * b)==0:
        return 1
    else:
        return 0
    
def puerta_nor(a, b):
    # La operación NOR es 1 si a es 1 o b es 1.
    if a == 1 or b == 1:
        return 0
    else:
        return 1
    
def puerta_xor(a, b):
    # La operación XOR es 1 si a es 1 o b es 1.
    if a == b:
        return 0
    if a != b:
        return 1

# --- Interfaz de usuario ---
print("Simulador de Puertas Lógicas Básicas")
print("-------------------------------------")

# Puerta AND
entrada_a = int(input("Ingresa el primer valor para AND (0 o 1): "))
entrada_b = int(input("Ingresa el segundo valor para AND (0 o 1): "))
resultado_and = puerta_and(entrada_a, entrada_b)
print(f"El resultado de {entrada_a} AND {entrada_b} es: {resultado_and}\n")

# Puerta OR
entrada_a = int(input("Ingresa el primer valor para OR (0 o 1): "))
entrada_b = int(input("Ingresa el segundo valor para OR (0 o 1): "))
resultado_or = puerta_or(entrada_a, entrada_b)
print(f"El resultado de {entrada_a} OR {entrada_b} es: {resultado_or}\n")

# Puerta NOT
entrada_a = int(input("Ingresa el valor para NOT (0 o 1): "))
resultado_not = puerta_not(entrada_a)
print(f"El resultado de NOT {entrada_a} es: {resultado_not}\n")

# Puerta NAND
entrada_a = int(input("Ingresa el primer valor para NAND (0 o 1): "))
entrada_b = int(input("Ingresa el segundo valor para NAND (0 o 1): "))
resultado_nand = puerta_nand(entrada_a, entrada_b)
print(f"El resultado de {entrada_a} NAND {entrada_b} es: {resultado_nand}\n")

# Puerta NOR
entrada_a = int(input("Ingresa el primer valor para NOR (0 o 1): "))
entrada_b = int(input("Ingresa el segundo valor para NOR (0 o 1): "))
resultado_nor = puerta_nor(entrada_a, entrada_b)
print(f"El resultado de {entrada_a} NOR {entrada_b} es: {resultado_nor}\n")

# Puerta XOR
entrada_a = int(input("Ingresa el primer valor para XOR (0 o 1): "))
entrada_b = int(input("Ingresa el segundo valor para XOR (0 o 1): "))
resultado_xor = puerta_xor(entrada_a, entrada_b)
print(f"El resultado de {entrada_a} XOR {entrada_b} es: {resultado_xor}\n")