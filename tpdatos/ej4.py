contactos = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

buscar = input("Ingrese el nombre del contacto que desea buscar: ")

if buscar in contactos:
    print(f"El número de {buscar} es: {contactos[buscar]}")
else:
    print(f"No se encontró el contacto '{buscar}'")
