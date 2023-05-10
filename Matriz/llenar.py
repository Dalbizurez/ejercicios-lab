def sumar(matriz):
    acumulabe = 0
    for x in matriz:
        for y in x:
            acumulabe += y
    return acumulabe

try:
    filas = int(input("Ingrese el numero de filas que desea: "))
    col = int(input("Ingrese el numero de columnas que desea: "))
except:
    print("Por favor ingrese un numero entero")
else:
    matriz = [[0 for i in range(col)] for j in range(filas)]
    for x in range(filas):
        for y in range(col):
            matriz[x][y] = int(input(f"Ingrese el valor {x},{y}: ")) 

    for x in matriz:
        print(x)
    print(x for x in matriz)
    print(sumar(matriz))

# Otra forma
#    matrix = []
#    for x in range(filas):
#        columna = []
#        for y in range(col):
#            columna.append(int(input(f"Ingrese el valor {x},{y}: ")))
#        matrix.append(columna)
#    for x in matrix:
#        print(x)
#    print(sumar(matrix))