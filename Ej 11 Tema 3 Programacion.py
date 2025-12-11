numero = input("Ingrese un número: ")
longitud = len(numero)
suma = sum(int(digito) ** longitud for digito in numero)
if suma == int(numero):
    print(f"{numero} es un número de Armstrong.")
else:
    print(f"{numero} no es un número de Armstrong.")
