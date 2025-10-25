productos=[]

for i in range(5):
    prod=input(f"ingrese el producto{i+1}:")
    productos.append(prod)

prodord=sorted(productos)
    
print(prodord)

elim=input("Que elemento desea eliminar?")

if elim in prodord:
    prodord.remove(elim)
else:
    print("el producto no se encuentra :p")

print(prodord)