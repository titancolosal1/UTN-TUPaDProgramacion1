notas=[4,2,4,2,6,1,8,9,9,8]

print(notas)

suma=0
alta=0
baja=notas[0]

for i in notas:
    suma=suma+i
    if i>alta:
        alta=i
    if i<baja:
        baja=i

print(f"el promedio es: {suma/len(notas)}")
print(f"la mas alta es: {alta}")
print(f"la mas baja es: {baja}")