num1 = int(input("ingrese numero"))
num2 = int(input("ingrese otro numero"))

sum = (num1+num2)
res = (num1-num2)
mul = (num1*num2)
div = (num1/num2)

if (num1==0 or num2==0):
    print ("invalido")

print (sum,"\n",res,"\n",mul,"\n",div)
