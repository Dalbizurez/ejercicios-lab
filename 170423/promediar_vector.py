numeros = []

def ingresar(arreglo, valor):
    arreglo.append(valor)

def media(arreglo):
    suma = 0
    for x in range(len(arreglo)):
        suma += numeros[x]
    promedio = suma/len(arreglo)
    return promedio
x = 0
while x<10:
    x += 1
    try:
        ingresar(numeros, int(input(f"Ingrese el valor {x}: ")))
    except:
        print("Por favor ingrese un valor entero")
        x -= 1
print(f"Promedio: {media(numeros)}")