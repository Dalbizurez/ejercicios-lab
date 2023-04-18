# Insertion sort
# Se trata de tomar un elemento de la lista y ordenarlo respecto a los elementos previos a el
# Moviendo los elementos mayores (O menores segun el caso) hacia la derecha del arreglo

def insertion(arreglo):
    x = 1
    while x<len(arreglo):
        y = x
        while y > 0 and arreglo[y-1]>arreglo[y]:
            valor = arreglo[y]
            arreglo[y] = arreglo[y-1] 
            arreglo[y-1] = valor
            y -= 1
        x += 1
    return arreglo

# Bubble Sort
# Se trata de simular como los valores mas pequeños "suben" dentro del arreglo hasta llegar al prinicipio del arreglo
def bubble(arreglo):
    x = 1
    for x in range(1, len(arreglo)):
        y = 0
        for y in range(len(arreglo)-x):
            if arreglo[y] > arreglo[y+1]:
                mayor = arreglo[y]
                arreglo[y] = arreglo[y+1]
                arreglo[y+1] = mayor
    return arreglo

# QuickSort
# Se trata de escoger un valor aleatorio del arreglo, considerado el pivote
# El cual es comparado con el resto del arreglo
# De manera que los valores menores al pivote se pasan a la izquierda de este
# Y los mayores a la derecha del pivote
# Esto se repite en los sectores alrededor del pivote hasta que el arreglo este ordenado
def quicksort(arreglo, inicio, fin):
    if inicio < fin:
        index = partition(arreglo, inicio, fin)
        quicksort(arreglo, inicio, index-1)
        quicksort(arreglo, index+1, fin)
    return arreglo
def partition(arreglo, inicio, fin):
    part_index = inicio
    pivote = arreglo[fin]
    for x in range(inicio, fin):
        if arreglo[x] <= pivote:
            temporal = arreglo[part_index]
            arreglo[part_index] = arreglo[x]
            arreglo[x] = temporal
            part_index += 1
    arreglo[fin] = arreglo[part_index]
    arreglo[part_index] = pivote
    return part_index

# Selection Sort
# Se trata de tomar un valor, compararlo con los demas, si es menor
# colocarlo al principio, tomar el siguiente valor mas bajo, compararlo y si es menor colocarlo despues del primero
# Esto se repite hasta que este ordenado
def selection(arreglo):
    for x in range(0, len(arreglo)):
        menor = arreglo[x]
        indice_min = x
        for y in range(indice_min, len(arreglo)):
            if arreglo[y]<menor:
                indice_min = y
                menor = arreglo[y]
        temp = arreglo[indice_min]
        arreglo[indice_min] = arreglo[x]
        arreglo[x] = temp
    return arreglo
def ingresar(arreglo, valor):
    arreglo.append(valor)

inicial = [4,1,2,5,8,9,1,3,6,10,7]

print(f"Inicial {inicial}")
print(f"Insertion Sort: {insertion(inicial.copy())}")
print(f"Bubble Sort: {bubble(inicial.copy())}")
print(f"Quicksort: {quicksort(inicial.copy(), 0, len(inicial)-1)}")
print(f"Selection Sort: {selection(inicial.copy())}")

