def mas_alto():
    lista = []
    n = 0
    while n < 10:
        n = n + 1
        m = int(input('Dame valores para hacer una lista: '))
        lista.append(m)
        mas_alto=max(lista)
    print("Lista completa:", lista)
    print(f"El número más alto de la lista es: {mas_alto}")

# Llamar a la función
mas_alto()
