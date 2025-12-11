negativos = 0
positivos = 0
cantidadP = 0
cantidadN = 0
p=0
n=0
for i in range(12):
    numero = int(input("Ingrese un número : "))
    if numero >= 0:
        cantidadP += 1
        positivos += numero
        p=positivos/cantidadP
    else: 
        cantidadN += 1
        negativos += numero 
        n= negativos/cantidadN
# Imprimir resultados
print("Suma de números positivos:", p)
print("Suma de números negativos:", n)