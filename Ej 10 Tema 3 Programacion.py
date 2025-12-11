limite = int(input("Ingrese el límite: "))
suma = 0
N = 1

while suma <= limite:
    suma += N
    N += 1

print("El valor de N para el cual la suma excede el límite",limite," es: ",N-1)
