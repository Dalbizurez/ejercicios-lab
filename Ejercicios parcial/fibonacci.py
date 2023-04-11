
# La sucesion es A2 = A1 + A0
# An = A(n-1) + A(n-2)
# Donde A0 = 0 y A1 = 1
# n = a + b
def fibonacci(n):
    r = 0
    i = 0
    j = 1
    print(1)
    for x in range(n-1, 0, -1):
        r = i + j
        i = j
        j = r
        print(r)
        
    


try:
    n = int(input("Ingrese el numero de valores que desea ver: "))
except:
    print("Por favor ingrese un valor entero")
else:
    fibonacci(n)