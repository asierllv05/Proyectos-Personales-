def lista():
    m=0
    lista=[]
    cont=0
    while m<10:
        m=m+1
        n=int(input('Dame numeros para la lista: '))
        lista.append(n)
    print(lista)
    lista_ordenada = sorted(set(lista))
    print(lista_ordenada)
    if lista==lista_ordenada:
        return True
    else:
        return False


lista()