pares = 0
impares = 0
for i in range(10):
    numero = int(input("Ingrese un número positivo: "))
    if numero < 0:
        print("El número ingresado no es positivo. Intente nuevamente.")
        continue
    if numero % 2 == 0: 
        pares += numero
    else: 
        impares += numero
      

# Imprimir resultados
print("Suma de números pares:", pares)
print("Suma de números impares:", impares)

