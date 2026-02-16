pa=0
suma_edades = 0
cantidad_edades = 0
maximo = float('-inf') 
minimo = float('inf') 
while True:
    edad = int(input("Ingrese la edad de la gente (o escriba un numero negativo para terminar): "))
    numero = int(edad)
    if numero >= 0:
        maximo = max(maximo, numero)
        minimo = min(minimo, numero)
    if edad < 0:
        break
    elif edad >= 18 and edad <= 65:
        pa += 1
    if edad > 0:
        suma_edades += edad
        cantidad_edades += 1
        media_edades = suma_edades / cantidad_edades

print(f"La media de las edades ingresadas es: {media_edades}")
print('La poblacion Activa es :',pa)
print(f"La edad maxima es: {maximo}")
print(f"La edad minima es: {minimo}")