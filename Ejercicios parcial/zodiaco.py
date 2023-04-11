# Ingresar un  numero de 1 a 365, decir dia, mes y signo del zodiaco

def zodiaco(dia):
    signo = ""
    # Capricornio 22 de diciembre a 20 de enero
    if dia <= 20 or (dia <= 365 and dia >= 356):
        signo = "Capricornio"
    # Acuario 21 de enero a 19 de febrero
    elif dia >= 21 and dia <= 50:
        signo = "Acuario"
    # Piscis 20 de febrero a 20 de marzo
    elif dia >= 51 and dia <= 79:
        signo = "Piscis"
    # Aries 21 de marzo a 20 de abril
    elif dia >= 80 and dia <= 110:
        signo = "Aries"
    # Tauro 21 de abril a 20 de mayo
    elif dia >= 111 and dia <= 140:
        signo = "Tauro"
    # Geminis 21 de mayo a 20 de junio
    elif dia >= 141 and dia <= 171:
        signo = "Geminis"
    # Cancer 21 de junio a 22 de julio
    elif dia >= 172 and dia <= 202:
        signo = "Cancer"
    # Leo 23  de julio a 23 de agosto
    elif dia >= 204 and dia <= 235:
        signo = "Leo"
    # Virgo 24  de agosto a 22 de septiembre
    elif dia >= 236 and dia <= 265:
        signo = "Virgo"
    # Libra 23 de septiembre a 22 de octubre
    elif dia >= 266 and dia <= 295:
        signo = "Libra"
    # Escorpio 23 de octubre a 22 de noviembre
    elif dia >= 296 and dia <= 326:
        signo = "Escorpio"
    # Sagitario 23 de noviembre a 21 de diciembre
    elif dia >= 327 and dia <= 255:
        signo = "Sagitario"

    return signo

def fecha(dia):
    mes = ""
    if dia <= 31:
        mes = "Enero"
    elif dia >= 32 and dia <= 59:
        mes = "Febrero"
        dia -= 31
    elif dia >= 60 and dia <= 90:
        mes = "Marzo"
        dia -= 59
    elif dia >= 91 and dia <= 120:
        mes = "Abril"
        dia -= 90
    elif dia >= 121 and dia <= 151:
        mes = "Mayo"
        dia -= 120
    elif dia >= 152 and dia <= 181:
        mes = "Junio"
        dia -= 150
    elif dia >= 182 and dia <= 212:
        mes = "Julio"
        dia -= 181
    elif dia >= 213 and dia <= 243:
        mes = "Agosto"
        dia -= 212
    elif dia >= 244 and dia <= 273:
        mes = "Septiembre"
        dia -= 243
    elif dia >= 274 and dia <= 304:
        mes = "Octubre"
        dia -= 273
    elif dia >= 305 and dia <= 334:
        mes = "Noviembre"
        dia -= 304
    elif dia >= 335 and dia <= 365:
        mes = "Diciembre"
        dia -= 334

    return mes, dia

try:
    dia = int(input("Ingrese el dia a determinar: "))
except:
    print("Solo se aceptan numeros enteros")
else:
    if dia <= 365 and dia > 0:
        print(zodiaco(dia))
        print(fecha(dia))
    