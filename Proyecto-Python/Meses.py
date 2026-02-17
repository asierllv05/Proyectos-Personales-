numero = int(input("Por favor, ingresa un número entre 1 y 12: "))

if 1 <= numero <= 12:
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    mes_correspondiente = meses[numero - 1]
    print("El número",numero,"corresponde al mes de ",mes_correspondiente)
else:
    print("Error: El número debe estar entre 1 y 12.")
