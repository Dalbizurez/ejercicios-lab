import random

# Cantidad de columnas
COL = 4
# Cantidad de filas
ROW = 4

# Matriz para llenar 
matriz = []

# Funcion para buscar un valor en la matriz
# Retorna la cantidad de veces que se encuentra el valor y la posicion del valor
def buscar(matrix, valor):
    matches = 0
    posicion = []
    #x = 0
    #for row in matrix:
    #    x += 1
    #    y = 0
    #    for col in row:
    #        y += 1
    #        if col == valor:
    #            matches += 1
    #            posicion.append(f"{x}, {y}")
    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == valor:
                matches += 1
                posicion.append(f"{y}, {x}")

    return matches, posicion

# Ciclo for que rellena la matriz con valores aleatorios
for x in range(ROW):
    fila = []
    for y in range(COL):
        fila.append(random.randint(1,50))
    matriz.append(fila)

# El numero de intentos del usuario
intentos = 0 
# El numero de aciertos
aciertos = 0
# Vector para almacenar los valores intentados
ingresados = []
# El total de valores que hay en la matriz
total = COL * ROW
# Mientras el numero de aciertos sea menor al total
while aciertos<total:
    intentos += 1
    print("Por favor ingrese un numero entero")
    try:
        numero = int(input())
    except:
        continue
    else:
        if numero in ingresados:
            print("Ya has intentado este numero")
            continue
        ingresados.append(numero)
        acierto, posicion = buscar(matriz, numero)
        if acierto>=1: 
            aciertos += acierto
            for p in posicion:
                print(f"Acierto! {numero} en {p}")
        else:
            print(f"Fallo! Números ingresados {ingresados}")
        print(f"Faltan {total-aciertos} numeros")
print(f"Has acertado todos los numeros, felicidades. Intentos: {intentos}")