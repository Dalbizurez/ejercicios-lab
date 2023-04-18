numeros = []

def ingresar(arreglo, valor):
    arreglo.append(valor)

def buscar(arreglo, valor):
    for x in range(len(arreglo)):
        if arreglo[x] == valor:
            return x
    return -1

x = 0
while x<10:
    x += 1
    try:
        ingresar(numeros, int(input(f"Ingrese el valor {x}: ")))
    except:
        print("Por favor ingrese un valor entero")
        x -= 1
try:

    x = buscar(numeros, int(input("Ingrese el valor a buscar: ")))
except:
    print("Por favor ingrese un valor entero")
else:
    if x>-1:
        print(numeros)
        print(f"El valor se encuentra en la posicion {x+1}")
    else:
        print("Valor no encontrado")