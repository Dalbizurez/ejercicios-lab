numeros = []

def ingresar(arreglo, valor):
    arreglo.append(valor)


def buscar(arreglo, valor):
    for x in range(len(arreglo)):
        if arreglo[x] == valor:
            return x
    return -1

try:
    nums = int(input("Cuantos numeros desea ingresar: "))
except:
    print("Ingrese un valor entero")

if nums>100:
    print("Debe ser menor a 100, se solicitaran 100")
    x = 100

x = 0
while x<nums:
    x += 1
    try:
        ingresar(numeros, int(input(f"Ingrese el valor {x}: ")))
    except:
        print("Por favor ingrese un valor entero")
        x -= 1
while True:
    try:

        x = buscar(numeros, int(input("Ingrese el valor a buscar: ")))
    except:
        break
    else:
        if x>-1:
            print(numeros)
            print(f"El valor se encuentra en la posicion {x+1}")
        else:
            print("Valor no encontrado")