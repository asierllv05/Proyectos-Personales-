
valor1 = float(input("Por favor, ingrese el primer valor: "))
valor2 = float(input("Por favor, ingrese el segundo valor: "))
valor3 = float(input("Por favor, ingrese el tercer valor: "))

maximo = valor1
minimo = valor1

if valor2 > maximo:
    maximo = valor2
elif valor2 < minimo:
    minimo = valor2

if valor3 > maximo:
    maximo = valor3
elif valor3 < minimo:
    minimo = valor3

print("El máximo es", maximo,"el mínimo es", minimo)
