num=0
par=0
imp=0
pos=0

for i in range(1,11):
    num=int(input("ingrese numero"))
    if num&2==0 or num==2:
        par=par+1
    if num&2==1:
        imp=imp+1
    if num>0:
        pos=pos+1

print(f"Hay {par} pares,{imp} impares y {pos} positivos")