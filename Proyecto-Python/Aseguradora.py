# Leer la edad del asegurado
edad = int(input("Ingrese la edad del asegurado: "))

# Verificar que el asegurado tiene al menos 18 años
if edad < 18:
    print("No se puede asegurar a personas menores de 18 años.")
else:
    # Leer los años de experiencia de conducción
    experiencia = int(input("Ingrese los años de experiencia de conducción: "))

    # Leer el número de accidentes
    accidentes = int(input("Ingrese el número de accidentes: "))

    # Calcular el importe base del seguro
    importe_base = 300

    # Calcular los incrementos en función de los años de experiencia
    if experiencia < 3:
        importe_base += 200
    elif 3 <= experiencia < 5:
        importe_base += 150
    elif 5 <= experiencia <= 10:
        importe_base += 100

    # Sumar 200 euros si la edad del asegurado es menor de 25 años
    if edad < 25:
        importe_base += 200
    # Calcular el importe adicional en función del número de accidentes
    if accidentes == 1:
        importe_base += 50
    elif accidentes == 2:
        importe_base += 125
    elif accidentes == 3:
        importe_base += 225
    elif accidentes == 4:
        importe_base += 375
    elif accidentes == 5:
        importe_base += 575
    elif accidentes >= 6:
        importe_base *= 0
    elif accidentes < 0:
        importe_base -= 100000 

if importe_base==0:
    print("No lo podemos asegurar")
elif importe_base > 300:
    print("El importe total del seguro es de",importe_base,"euros.")
elif importe_base<=0:
    print("Dame un valor de accidentes positivo")