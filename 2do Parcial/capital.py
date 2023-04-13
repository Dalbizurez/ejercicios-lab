# Capital = capital + capital*interes

def capital(capital, interes):
    capital_inicial = capital
    tiempo = 0
    while capital < capital_inicial*2:
        print(f"Capital al año {tiempo} de inversion: {capital}")
        capital += capital*interes
        tiempo += 1
    print(f"Capital al año {tiempo} de inversion: {capital}")
    return tiempo

try:
    inversion = float(input("Capital inicial: "))
    interes = float(input("Interes: "))
except:
    print("Ingrese solo numeros decimales")
else:
    print(capital(inversion, interes/100))

# Ejemplo 1: P.E: C: 100. R: 9% Años: 9
# Ejemplo 2: P.E: C: 350. R: 5% Años: 15
# Ejemplo 3: P.E: C: 1500. R: 7.5% Años: 10
# Ejemplo 4: P.E: C: 350. R: 7.5% Años: 10
# Ejemplo 5: P.E: C: 75.25. R: 8% Años: 10