# Leer la cantidad de litros de agua consumidos
litros_consumidos = float(input("Ingrese la cantidad de litros de agua consumidos: "))
if litros_consumidos < 0:
    print("Error: La cantidad de litros consumidos no puede ser menor que 0.")
else:
    costo = 0

    if litros_consumidos <= 50:
        costo = 0
    elif litros_consumidos <= 200:
        costo = (litros_consumidos - 50 )* 0.10  
    else:
        costo = litros_consumidos * 0.30  
    if costo < 6:
        costo = 6  
    print("El costo de la factura de agua es de",costo,"euros.")

