import random

num1=random.randint(0,9)
num2=0
cont=0

while num1!=num2:
    cont=cont+1
    num2=int(input("ingrese numero"))

    if num1==num2:
        print(f"Correcto,se necesitaron {cont} intentos")
        break