# Determinar el numero menor
def menor(n1, n2):
    if n1 > n2:
        menor = n2
    elif n1 < n2:
        menor = n1
    else:
        menor = 0
    return menor

# Determinar el mayor
def mayor(n1, n2):
    if n1 > n2:
        mayor = n1
    elif n1 < n2:
        mayor = n2
    else:
        mayor = 0
    return mayor

# Hallar el promedio (Media aritmetica)
def  promedio(n1, n2):
    return (n1+n2)/2

# Identificar si un numero es primo
def primo(n):
    x = 2
    primo = 0
    while x<=n/2:
        primo += 1 if n%x == 0 else 0
        x += 1
    return primo == 0

# Hallar el MCD
def mcd(n1, n2):
    dividendo = mayor(n1, n2)
    divisor = menor(n1, n2)
    if divisor != 0:
        residuo = dividendo/divisor
        while True:
            residuo = dividendo % divisor
            dividendo = divisor
            if residuo == 0:
                break
            divisor = residuo
        mcd = divisor

    else:
        mcd = n1
    return mcd

# Inicio del programa
while True:
    try:
        n1 = int(input("Numero 1: "))
        n2 = int(input("Numero 2: "))
    except:
        print("Por favor ingrese numeros enteros")
    else:
    # Despliegue de menu
        print("Ingrese la letra correspondiente a la opcion que desea seleccionar")
        print("A. Menor\nB. Mayor\nC. Media\nD. Primo\nE. MCD\nF. Salir")
        match input("Seleccione la opcion que desea: "):
            case "A" | "a":
                operacion = "hallar el menor"
                n_menor = menor(n1, n2)
                resultado =  " son iguales" if n_menor == 0 else n_menor
            case "B" | "b":
                operacion = "hallar el mayor"
                n_mayor = mayor(n1, n2)
                resultado =  " son iguales" if n_mayor == 0 else n_mayor
            case "C" | "c":
                operacion = "hallar la media aritmetica"
                resultado = promedio(n1, n2)
            case "D" | "d":
                operacion = "identificar si son primos"
                resultado1 = f"{n1}"
                resultado2 = f"{n2}"
                if primo(n1):
                    resultado1 += " es primo"
                else:
                    resultado1 += " no es primo"
                if primo(n2):
                    resultado2 += " es primo"
                else:
                    resultado2 += " no es primo"
                resultado = f"{resultado1} y {resultado2}"
            case "E" | "e":
                operacion = "hallar MCD"
                resultado = mcd(n1, n2)

            case "F" | "f":
                break
            case _:
                print("Opcion no reconocida")
        input(f"Selecciono {operacion}, el resultado es: {resultado}")