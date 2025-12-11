def obtener_segundo_mas_alto():
    lista = []
    n = 0
    while n < 10:
        n = n + 1
        m = int(input('Dame valores para hacer una lista: '))
        lista.append(m)

    # Verificar si hay al menos dos números en la lista
    if len(lista) < 2:
        print("La lista debe contener al menos dos números.")
    else:
        # Eliminar duplicados y ordenar la lista en orden descendente
        lista_ordenada = sorted(set(lista), reverse=True)

        # Imprimir el segundo número más alto
        segundo_mas_alto = lista_ordenada[1]
        print("Lista completa:", lista)
        print(f"El segundo número más alto de la lista es: {segundo_mas_alto}")

# Llamar a la función
obtener_segundo_mas_alto()