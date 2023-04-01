def procesarNombre( nombre: str):
    return nombre.casefold(), nombre.upper(), nombre.title()

def procesarTelefono(tel: str):
    return tel[4:-3]
    
def procesarCompra(cesta: str):
    resultado = ""
    for x in cesta.split(","):
        resultado += x.strip() + "\n"
    return resultado
    #return cesta.split(",")

def palindromo(palabra: str):
    return palabra == palabra[::-1]

def sustituirChar(palabra: str, char1: str, char2: str):
    return palabra.replace(char1, char2)

def contarPalabras(frase: str):
    return len(frase.split())

def caracteres(texto: str):
    resultado = ""
    for c in texto:
        resultado += c + "\n"
    return resultado[:-1]

def menu():
    print("1. Ingresar nombre y mostrar diferentes formas de capitalizacion\n2. Ingresar un telefono y quitar prefijo y extension\n3. Procesar una lista de compras\n4. Identificar un Palindromo\n5. Sustituir un caracter\n6. Contar palabras\n7. Mostrar caracteres 1 por 1")
    opcion = input("Ingres la opcion que desea ejecutar: ")
    resultado = ""
    match opcion:
        case "1":
            nombre = input("Ingrese su nombre completo: ")
            resultado = ""
            for x in procesarNombre(nombre):
                resultado += x + "\n"
        case "2":
            telefono = input("Ingrese el numero de telefono a procesar: ")
            if telefono.find("+34"):
                resultado = procesarTelefono(telefono)
            else:
                resultado = "Codigo de area faltante"
        case "3":
            cesta = input("Ingrese la lista de compras, separando cada objeto usando una coma: ")
            resultado = procesarCompra(cesta)
        case "4":
            palabra = input("Ingrese la palabra: ")
            resultado = "Palindromo" if palindromo(palabra) else "No es palindromo"
        case "5":
            palabra = input("Ingrese la palabra: ")
            c1 = input("Ingrese el caracter a buscar: ")
            c2 = input("Ingrese el caracter con el que se va a sustituir: ")
            if len(c1) == 1 and len(c2) == 1:
                resultado = sustituirChar(palabra, c1, c2)
            else:
                resultado = "Se ingreso más de un caracter en las opciones" 
        case "6":
            frase =  input("Ingrese una frase: ")
            resultado = contarPalabras(frase)
        case "7":
            texto = input("Ingrese el texto a trabajar: ")
            resultado = caracteres(texto)
        case _:
            resultado = "Opcion no reconocida"
    print()
    return resultado

salir = False
print("Bienvenido")
while not salir:
    print(menu())
    salir = input("Presione enter para reiniciar, ingrese cualquier cosa para salir\n")

# Pruebas:
#print(caracteres("the brown fox"))
#print(contarPalabras("the brown fox chases the bat"))
#print(sustituirChar("Daniel", "a", "4"))
#print("Palindromo" if palindromo("profesor roseforp") else "No es palindromo")
#print(procesarCompra("tomate, cebolla, cilantro, cereal, harina"))
#for x in procesarCompra("tomate, cebolla, cilantro, cereal, harina"):
#    print(x.strip())
#print(procesarTelefono("+34-58-56"))
#print(procesarNombre("daniel AlbizUrez alpIreZ"))
