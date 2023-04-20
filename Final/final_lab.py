#Daniel Albizurez Alpirez
#Denilson Carreto Mendez
import datetime

registro = []
campos = ["DPI", "Nombres", "Apellidos", "Fecha de nacimiento", "Numero de telefono celular", "Numero de telefono domiciliar", "Departamento de residencia", "Municipio de residencia", "Zona de residencia", "Direccion exacta", "Departamento de nacimiento", "Municipio de nacimiento", "Genero", "Estado Civil"]

edad = 0

def ingresar_dpi(dpi):
    try:
        int(dpi)
    except:
        return False
    else:
        if len(dpi) == 13:
            registro.append(dpi)
        else:
            return False
        return True

def ingresar_numero(num):
    try:
        int(num)
    except:
        return False
    else:
        registro.append(num)
    return True

def ingresar_texto(texto):
    if texto.isalpha():
        registro.append(texto)
        return True
    else:
        return False
    
def  ingresar_nacimiento(fecha):
    #fecha = fecha.split("/")
    try:
        nacimiento = datetime.datetime.strptime(fecha,"%d/%m/%y")
    except:
        return False
    else:
        hoy = datetime.datetime.now()
        edad = (nacimiento - hoy).days//365
        registro.append(nacimiento.strftime("%d-%m-%y"))
        return True
    
def genero(inicial):
    if inicial == "M":
        registro.append("Masculino")
    elif inicial == "F":
        registro.append("Femenino")
    else:
        return False
    return True

def estado(inicial):
    if inicial == "S":
        registro.append("Soltero")
    elif inicial == "C":
        registro.append("Casado")
    else:
        return False
    return True

print("Bienvenido al registro, debe ser mayor de edad para participar")
print("Por favor ingrese los datos solicitados")



resultado = True
contador = 0
while contador<14:
    print(f"Por favor ingrese {campos[contador]}")
    match contador:
        case 0:
            dato = input("El DPI debe ser 13 numeros:\n")
            resultado = ingresar_dpi(dato)
        case 1:
            dato = input("Los nombres deben ser solo letras\n")
            resultado = ingresar_texto(dato)
        case 2:
            dato = input("Los apellidos deben ser solo letras\n")
            resultado = ingresar_texto(dato)
        case 3:
            dato = input("Ingrese la fecha en formato d/m/yy\n")
            resultado = ingresar_nacimiento(dato)
        case 4:
            dato = input("El numero de celular solo debe contener numeros\n")
            resultado = ingresar_numero(dato)
        case 5:
            dato = input("El numero de casa solo debe contener numeros\n")
            resultado = ingresar_numero(dato)
        case 6 | 10:
            dato = input("El departamento deber ser solo letras\n")
            resultado = ingresar_texto(dato)
        case 7 | 11:
            dato = input("El Municipio deber ser solo letras\n")
            resultado = ingresar_texto(dato)
        case 8:
            dato = input("Solo debe ingresar el numero de la zona\n")
            resultado = ingresar_numero(dato)
        case 9:
            dato = input()
            registro.append(dato)
        case 12:
            dato = input("Por favor solo ingrese 'M' para seleccionar Masculino o 'F' para Femenino\n")
            resultado = genero(dato)
        case 13:
            dato = input("Por favor ingrese 'S' para seleccionar Soltero o 'C' para Casado\n")
            resultado = estado(dato)
    if resultado:
        contador += 1
    else:
        print(f"El dato ingresado no cumple el formato para {campos[contador]}")
        print("Por favor vuelva a intentarlo")

print("Registro exitoso")
for x in range(0, len(registro)):
    print(f"{campos[x]}: {registro[x]}")


#print(registro)