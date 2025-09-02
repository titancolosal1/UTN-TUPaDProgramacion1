num=1
sum=0
while num!=0:
    num=int(input("ingrese numero/o ingrese 0 para detener"))
    sum=sum+num
    if num==0:
        print(sum)
        break