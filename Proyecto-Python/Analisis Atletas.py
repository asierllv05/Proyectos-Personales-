# Leer el sexo del atleta
sexo = input("Ingrese el sexo del atleta (H para hombre, M para mujer): ").upper()
if sexo != "H" and sexo != "M":
    print("Error: Sexo no válido. Debe ser 'H' o 'M'.")
else:
    edad = int(input("Ingrese la edad del atleta: "))
    if edad < 0:
        print("Error: Edad no válida. Debe ser un número positivo.")
    else:
        tiempo = int(input("Ingrese el tiempo del atleta en minutos: "))
        if tiempo < 0:
            print("Error: Tiempo no válido. Debe ser un número positivo.")
        else:
            seleccionado = False

            if sexo == "H":
                if edad < 40 and tiempo <= 150:
                    seleccionado = True
                elif edad >= 40 and tiempo <= 175:
                    seleccionado = True
            else:
                if tiempo <= 180:
                    seleccionado = True
            if seleccionado:
                print("Seleccionado")
            else:
                print("No seleccionado")
