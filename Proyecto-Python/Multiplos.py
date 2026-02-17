N = int(input("Ingrese un número entero N: "))
if N < 1:
    print("Por favor, ingrese un número entero positivo.")
else:
    print("Múltiplos de 7 entre 1 y", N, ":")
    for i in range(1, N + 1):
        if i % 7 == 0 and i%3 != 0:
            print(i)
