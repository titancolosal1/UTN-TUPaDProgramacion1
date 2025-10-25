datos=[1,3,5,3,7,1,9,5,3]
visto=[]
rep=[]

for i in datos:
    if i in visto:
        if i not in rep:
            rep.append(i)
    else:
        visto.append(i)


print(visto)