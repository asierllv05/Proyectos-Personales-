s=int(input('Dame la cantidad de segundos que desea transformar:'))
if s>0:
    d=s//86400
    r=s%86400
    h=r//3600
    a=r%3600
    m=a//60
    b=a%60
    print('La duracion equivalente es',d,':',h,':',m,':',b)
elif s<0:
    print('Solo valores positivos')

