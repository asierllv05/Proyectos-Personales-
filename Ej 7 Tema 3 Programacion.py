
numeros = []
for i in range(1, 13):
    numero = float(input(f"Ingrese el número real {i}: "))
    numeros.append(numero)
maximo = max(numeros)
print(f"El máximo de los números ingresados es: {maximo}")
