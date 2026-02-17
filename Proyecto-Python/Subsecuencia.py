def subsecuencia3():
    n=int(input('Dame la longitud deseada de la subcadena: '))
    v=input('Dame la cadena: ')
    z=len(v)
    x=0
    for i in range(z):
        if i+2==z:
            x=-1
            break
        else:
            while v[i] != v [n]:
                i += 1
                x = v[i:n]
            return x
            
subsecuencia3()