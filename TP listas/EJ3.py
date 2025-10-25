import random
numeros=[]

for i in range(15):
    num=random.randint(1,100)
    numeros.append(num)

print(numeros)

pares=[]
impares=[]

for i in numeros:
    if i%2==0:
        pares.append(i)
    if i%2==1:
        impares.append(i)

print(f"hay {len(pares)} pares")
print(f"hay {len(impares)} impares")