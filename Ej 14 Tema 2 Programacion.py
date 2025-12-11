print("¡Bienvenido al recomendador de frutas!")
color = input("¿Que color tiene la fruta(Rojo/Amarillo/Verde): ")
if color == "Rojo":
    tamañoRojo = input("¿Que tamaño tiene la fruta (Pequeño/mediano): ")
    if tamañoRojo == "Mediano":
        print("Te recomiendo una manzana.")
    elif tamañoRojo == "Pequeño":
        FrutaPequeñaRoja= input("Que sabor tiene la fruta (dulce/acida) :")
        if FrutaPequeñaRoja == "dulce":
            print("Te recomiendo una Cereza")
        else:
            print("Te recomiendo una Uva")
elif color == "Verde":
    tamañoVerde = input("¿Que tamaño tiene la fruta (Grande/Mediano/Pequeño:")
    if tamañoVerde == "Mediano":
        print("Te recomiendo una manzana.")
    elif tamañoVerde == "Pequeño":
        print("Te recomiendo una Uva")
    else:
        print("Te recomiendo un Melon")
elif color == "Amarillo":
    forma = input("¿Que forma tiene(Redonda/Alargada):")
    if forma == "Alargada":
        print("Te recomiendo un Platano.")
    elif forma == "Redonda":
        tamañoAmarillo=input("Que tamaño tiene la fruta (Grande/Pequeño):")
        if tamañoAmarillo == "Grande":
            print("Te recomiendo un Pomelo")
        else:
            print("Te recomiendo un Limon")
else:
    print("Dame uno de los colores que pone")
