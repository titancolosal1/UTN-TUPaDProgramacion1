numeros=[1,2,3,4,5,6,7]
print(f"lista inicial: {numeros}")

ultimo=numeros.pop()

numeros.insert(0,ultimo)

print(f"lista final: {numeros}")