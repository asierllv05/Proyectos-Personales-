def lista():
    m=0
    lista=[]
    cont=0
    a=int(input('Dame la longitud de la lista: '))
    while m<a:
        m=m+1
        n=int(input('Dame numeros para la lista: '))
        lista.append(n)
        print(lista)
        if n%2!=0 and m%2==0:
            cont += 1
    print(f'La lista {lista} tiene {cont} numeros impares en posiciones pares')