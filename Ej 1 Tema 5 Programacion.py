def lista():
    cont=0
    m=0
    lista=[]
    b=int(input('Dame el numero a analizar'))
    while m<10:
        m=m+1
        n=int(input('Dame numeros para la lista'))
        lista.append(n)
        if n==b:
            cont+=1
    print(f'La lista {lista} tiene {cont} {b}')