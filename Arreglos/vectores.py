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
print(impares_mayor3(numeros))
print(impares_mayor3_2(numeros))

print(promedio(eliminar_menor(numeros)))