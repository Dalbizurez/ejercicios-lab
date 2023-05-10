# Vector para almacenar cada equipo
equipos = []
# Vector con el nombre de cada campo
CAMPOS = ["Nombre del equipo", "Partidos Ganados", "Partidos Empatados", "Partidos Perdidos",
          "Partidos Jugados", "Total de puntos"]
# Vector con el nombre de cada columna para el archivo csv
ABREVIATURAS = ["Nombre", "PG", "PE", "PP", "PJ", "TP"]

# Funcion para guardar los datos en el vector equipos
def ingresar(nombre, ganados, empatados, perdidos):
    equipo = []
    equipo.append(nombre)
    equipo.append(ganados)
    equipo.append(empatados)
    equipo.append(perdidos)

    jugados = ganados + empatados + perdidos
    puntos = (ganados * 3) + (empatados * 1) 
    equipo.append(jugados)
    equipo.append(puntos)

    equipos.append(equipo)

#    return jugados, puntos
# Funcion para imprimir el resumen de los equipos
def resumen(equipo):
    resumen = ""
    for x in range(len(equipo)):
        resumen += f"{CAMPOS[x]} ({ABREVIATURAS[x] if x != 0 else ''}): {equipo[x]}\n"
    return resumen

# Funcion para exportar el archivo csv
def exportar(equipos, nombre):

    doc = ""
    for col in ABREVIATURAS:
        doc += f"{col};"
    doc = doc[:-1]
    doc += "\n"
    for e in equipos:
        for x in e:
            fila += f"{x};"
        fila = fila[:-1]
        doc += fila + "\n"
    try:
        archivo = open(f"{nombre}.csv", "wt")
        archivo.write(doc)
        archivo.close()
    except:
        return False
    else:
        return True



print("Liga Nacional de Futbol Guatemala")
print("Bienvenido al control e posiciones")
while True:
    print("Para seleccionar las opciones ingrese el numero correspondiente")
    print("1. Ingreso de equipos y puntaje\n2.Exportar tabla de posiciones\n3.Salir")
    opcion = input("Que desea realizar: ")
    match opcion:
        case "1":
            while True:
                n = len(equipos)
                
                nombre = input("Ingrese el nombre del equipo: ")
                while True:
                    try:
                        ganados = int(input("Cantidad de partidos ganados: "))
                        empatados = int(input("Cantidad de partidos empatados: "))
                        perdidos = int(input("Cantidad de partidos perdidos: "))
                    except:
                        print("Por favor ingrese numeros enteros para cada partido")
                    else:
                        ingresar(nombre, ganados, empatados, perdidos)
                        print(resumen(equipos[n]))
                        break
                continuar = input("¿Desea ingresar otro equipo S/N?")
                if continuar == "N":
                    break
                elif continuar == "S":
                    continue
        case "2":
            if not exportar(equipos, input("Nombre del archivo: ")):
                print("Ha ocurrido un error inesperado, por favor vuelva a intentarlo")
            else:
                print("Archivo creado correctamente")
        case "3":
            break

