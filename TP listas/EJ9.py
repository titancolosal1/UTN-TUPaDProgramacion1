tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

jugador_actual = "X"

for turno in range(9):
    mostrar_tablero()
    print(f"Turno del jugador {jugador_actual}")

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("Casilla ocupada, intente de nuevo.")
        turno -= 1

mostrar_tablero()
