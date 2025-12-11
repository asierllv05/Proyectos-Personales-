duracion_segundos = int(input("Ingrese la duración de la llamada en segundos: "))
if duracion_segundos < 60:
    costo = 10  
else:
    minutos_completos = duracion_segundos // 60
    costo = 10 + (minutos_completos - 1) * 5  
print("El costo de la llamada es de",costo,"céntimos.")
