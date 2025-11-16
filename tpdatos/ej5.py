frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Cantidad de apariciones de cada palabra:", contador)
