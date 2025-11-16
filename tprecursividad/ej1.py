def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número entero positivo: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")
