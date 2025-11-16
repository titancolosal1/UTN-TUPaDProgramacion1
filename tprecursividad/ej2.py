# Función recursiva para calcular Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
