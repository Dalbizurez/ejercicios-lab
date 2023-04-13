# Ejercicio 1
numeros = [1,5,8,3,30,9,13]

def impares_mayor3(lista):
    impares = []
    for i in lista:
        if i%2 != 0 and i > 3:
            impares.append(i)
    return impares

def impares_mayor3_2(lista):
    return [i for i in lista if i%2 != 0 and i > 3]
#Fin ejercicio 1

# Ejercicio 2
def eliminar_menor(lista):
    menor = lista[1]
    for n in lista:
        if n<menor:
            menor =  n
    lista.remove(menor)
    return lista

def promedio(lista):
    resultado = 0
    for x in lista:
        resultado += x
    resultado /= len(lista)
    return resultado 
#Fin ejercicio 2

# Ejercicio 3
def invertir(vector):
    inverso = []
    for x in range(len(vector)-1, -1, -1):  
        inverso.append(vector[x])
    return inverso

def invertir2(vector):
    return vector[-1::-1]
#Fin ejercicio 3

print(impares_mayor3(numeros))
print(impares_mayor3_2(numeros))

print(promedio(eliminar_menor(numeros)))

ingresado = []
for x in range(0, 5):
    ingresado.append(input(f"Ingrese el valor {x+1}: "))
print(f"Ingreso {ingresado}")
print(f"Inverso {invertir(ingresado)}")
print(f"Inverso {invertir2(ingresado)}")