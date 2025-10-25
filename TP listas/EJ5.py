nombres=["juan","pedro","luis","jose","rmando","enrique","gustavo","leon"]

orden=input("ingresar 'add' para agregar un nombre,'del' para borrar uno o 'null' para no hacer nada")
name=""

if orden=="add":
    name=input("ingrese nombre")
    nombres.append(name)
if orden=="del":
    name=input("ingrese nombre")
    if name in nombres:
        nombres.remove(name)
    if name not in nombres:
        print("no se encuentra")
if orden=="null":
    print("Ok")
else:
    print("invalido")

print(nombres)