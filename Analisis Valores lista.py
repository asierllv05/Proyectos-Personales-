def lista():
    m=0
    lista=[]
    cont=0
    x=int(input('Dame un numero x: '))
    v=int(input('Dame numero n: '))
    while m<10:
        m=m+1
        n=int(input('Dame numeros para la lista: '))
        lista.append(n)
        if n<x and m-1<v:
            cont+=1
        print(f'La lista {lista} tiene {cont} numeros mas pequeños que x en n')
        
lista()