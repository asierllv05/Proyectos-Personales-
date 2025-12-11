cantidad_euros = int(input("Ingrese la cantidad de euros: "))
billetes_monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]
cantidad_500 = 0
cantidad_200 = 0
cantidad_100 = 0
cantidad_50 = 0
cantidad_20 = 0
cantidad_10 = 0
cantidad_5 = 0
cantidad_2 = 0
cantidad_1 = 0
if cantidad_euros >= 500:
    cantidad_500 = cantidad_euros // 500
    cantidad_euros %= 500

if cantidad_euros >= 200:
    cantidad_200 = cantidad_euros // 200
    cantidad_euros %= 200

if cantidad_euros >= 100:
    cantidad_100 = cantidad_euros // 100
    cantidad_euros %= 100

if cantidad_euros >= 50:
    cantidad_50 = cantidad_euros // 50
    cantidad_euros %= 50

if cantidad_euros >= 20:
    cantidad_20 = cantidad_euros // 20
    cantidad_euros %= 20

if cantidad_euros >= 10:
    cantidad_10 = cantidad_euros // 10
    cantidad_euros %= 10

if cantidad_euros >= 5:
    cantidad_5 = cantidad_euros // 5
    cantidad_euros %= 5

if cantidad_euros >= 2:
    cantidad_2 = cantidad_euros // 2
    cantidad_euros %= 2

cantidad_1 = cantidad_euros

print("Desglose mínimo en billetes y monedas:")
if cantidad_500 > 0:
    print(cantidad_500," billete(s) de 500 euros")
if cantidad_200 > 0:
    print(cantidad_200," billete(s) de 200 euros")
if cantidad_100 > 0:
    print(cantidad_100," billete(s) de 100 euros")
if cantidad_50 > 0:
    print(cantidad_50," billete(s) de 50 euros")
if cantidad_20 > 0:
    print(cantidad_20," billete(s) de 20 euros")
if cantidad_10 > 0:
    print(cantidad_10," billete(s) de 10 euros")
if cantidad_5 > 0:
    print(cantidad_5," billete(s) de 5 euros")
if cantidad_2 > 0:
    print(cantidad_2," moneda(s) de 2 euros")
if cantidad_1 > 0:
    print(cantidad_1," moneda(s) de 1 euro")
if cantidad_euros<0 :
    print("No hay monedas ni billetes")
