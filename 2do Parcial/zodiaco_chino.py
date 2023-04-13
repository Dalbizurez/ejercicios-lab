# El elemento se mantiene durante 2 años
# El animal se repite cada 12 años

# Se necesia evaluar el año
# Como cada 2 años se repite el elemento, los años correspondientes a cada elemento, siempre terminan en el mismo digito

# Como cada 12 años se repite el animal, se puede restar 12 al año ingresado hasta llegar al año inicial del ciclo (Que es 2024), respectivo a cada animal (Siendo de 2024 a 2036)

  
def zodiaco(year):
    signo = ""
    elemento = ""
    year = year%1900
    match year%10:
        case 4 | 5:
            elemento = "madera"
        case 6|7:
            elemento = "fuego"
        case 8|9:
            elemento = "tierra"
        case 0|1:
            elemento = "metal"
        case 2|3:
            elemento = "agua"

# Quiza tambien puedo hacerlo con mod, pero ya lo hice asi, si me da tiempo pruebo
    while year >= 36:
        year -= 12
    match year:
        case 24:
            signo = "rata"  
        case 25:
            signo = "buey"  
        case 26:
            signo = "tigre"  
        case 27:
            signo = "conejo"  
        case 28:
            signo = "dragon"  
        case 29:
            signo = "serpiente"  
        case 30:
            signo = "caballo"  
        case 31:
            signo = "oveja"  
        case 32:
            signo = "mono"  
        case 33:
            signo = "gallo"  
        case 34:
            signo = "perro"  
        case 35:
            signo = "cerdo"  
    return signo, elemento
#    if year > 2000:
#        year = year%2000
    
try:
    year = int(input("Ingrese el año a analizar: "))
except:
    print("Solo se aceptan numeros enteros")
else:
    print(zodiaco(year))