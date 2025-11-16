def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

test1 = "radar"
test2 = "python"

print(f"{test1} es palíndromo? {es_palindromo(test1)}")
print(f"{test2} es palíndromo? {es_palindromo(test2)}")
